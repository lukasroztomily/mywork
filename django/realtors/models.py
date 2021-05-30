from django.db import models
from django.utils.timezone import now

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=50)
    phote = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description  = models.TextField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=now)


    def __str__(self):
        return self.name
    