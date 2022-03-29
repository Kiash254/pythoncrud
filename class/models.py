from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    adm=models.CharField(max_length=20)
    career=models.CharField(max_length=40,blank=True)
    check=models.BooleanField(default=False)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'  name{self.name},   adm{self.adm}'
    class Meta:    
        ordering=['name']