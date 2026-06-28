from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    srno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)