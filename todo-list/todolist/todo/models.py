from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Todo(models.Model):
    PRIORITY = [
        (None, 'Please Choose'),
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]
    task = models.CharField(max_length=60)
    priority = models.CharField(max_length=20, choices=PRIORITY)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, related_name='todo')
    done = models.BooleanField(default=False)

