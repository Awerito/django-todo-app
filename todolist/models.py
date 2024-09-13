from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
