from django.contrib.auth.models import User
from django.db import models
import uuid

class MoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # add this line
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    Description = models.TextField()
    Price = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5


