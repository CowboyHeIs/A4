from django.shortcuts import render, redirect, reverse
from main.forms import MoodEntryForm
from main.models import MoodEntry
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime

#######################################
'SHOW'
#######################################
def show_xml(request):
    data = MoodEntry.objects.all()

def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MoodEntry.objects.all()

def show_json(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required(login_url='/login')
def show_main(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        mood_entries = MoodEntry.objects.filter(user=request.user)
        mood_entries_data = serializers.serialize('json', mood_entries)
        return JsonResponse(mood_entries_data, safe=False)

    mood_entries = MoodEntry.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'mood_entries': mood_entries,
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "main.html", context)
#######################################

#######################################
'PRODUCTS'
#######################################
def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        mood_entry = form.save(commit=False)
        mood_entry.user = request.user
        mood_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)

def edit_mood(request, id):
    # Get mood entry based on id
    mood = MoodEntry.objects.get(pk = id)

    # Set mood entry as an instance of the form
    form = MoodEntryForm(request.POST or None, instance=mood)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_mood.html", context)

def delete_mood(request, id):
    # Get mood based on id
    mood = MoodEntry.objects.get(pk = id)
    # Delete mood
    mood.delete()
    # Return to home page
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def create_mood_entry_ajax(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user
            mood_entry.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

#######################################

#######################################
'USER'
#######################################
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
#######################################