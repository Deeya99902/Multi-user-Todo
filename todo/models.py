from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    status_choices = [
       ('C', 'COMPLETED'),
       ('P','PENDING')
   ]
    priotrity_choices = [
       ('1','COMPLETED'),
       ('2','Pending'),
       ('3','PENDING'),
       ('4','PENDING'),
       ('5','PENDING'),
       ('6','PENDING'),
       ('7','PENDING'),
       ('8','PENDING'),
       ('9','PENDING'),
       ('10','PENDING'),
   ]
    title = models.CharField(max_length=50)
    status = models.CharField ( max_length=2, choices=status_choices )
    priority=models.CharField( max_length=2, choices=status_choices)
    date = models.DateField(auto_now_add=   True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    