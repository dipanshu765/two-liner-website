from django.db import models
from datetime import datetime

class Post(models.Model):
    title= models.CharField(max_length=20)
    content= models.TextField(max_length=2500)
    post_date= models.DateTimeField(default=datetime.now(), blank=True)
    writer= models.CharField(max_length=10, default='Dipanshu')
    def __str__(self):
        return self.title

