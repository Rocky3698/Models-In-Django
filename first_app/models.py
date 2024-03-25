from django.db import models
from django.utils import timezone
from datetime import datetime
from datetime import timedelta
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20, default='')  
    roll = models.IntegerField(default=0,primary_key=True)  
    father_name = models.CharField(max_length=20, default='')  
    address = models.TextField(default='')  
    # auto_field = models.AutoField(blank=True,null=True)
    date_field = models.DateField(default=datetime.today)  
    duration_field = models.DurationField(default=timedelta())   
    email_field = models.EmailField(default='example@gmail.com')
    null_boolean_field = models.BooleanField(default=None,null=True, blank=True)  
    time_field = models.TimeField(default=timezone.now)  
    url_field = models.URLField(default='http://google.com')
    def __str__(self) -> str:
        return f"Name : {self.name} Roll : {self.roll} Address : {self.address}"