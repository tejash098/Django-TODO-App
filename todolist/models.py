from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Status = models.CharField(max_length=100, choices=(('completed', 'Completed'), 
    ('pending', 'Pending'), 
    ('not_started', 'Not Started')), 
    default='not_started')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
