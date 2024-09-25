1. What is the difference between HttpResponseRedirect() and redirect()?
2. Explain how the MoodEntry model is linked with User!
3. What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.
4. How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.
5. Explain how did you implement the checklist step-by-step (apart from following the tutorial).

1. HttpResponseRedirect() creates 302 response while redirect() is a shortcut.
2. ForeignKey to the databse itself.
3. Authentication verifies identity while Authorization verifies user's permissions.
4. By having unique session ID for each user; other uses for cookies are preferences, items, and datas; Not all are safe.
5. I always had an error in tutorials, Am I tired for remaking it 27 times? yes. what did I gain from the errors? satisfaction of knowing what errors exists by experiencing it. Does it take a lot of my time? Of course.