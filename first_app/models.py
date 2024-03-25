from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length =20)
    roll=models.IntegerField(primary_key=True)
    father_name= models.CharField(max_length=20)
    address=models.TextField()

    def __str__(self) -> str:
        return f"Name : {self.name} Roll : {self.roll} Address : {self.address}"