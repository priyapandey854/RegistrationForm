from django.db import models

class Registration(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField()
    phone=models.CharField( max_length=15)
    gender = models.CharField(max_length=50, default="Not specified")
    message=models.TextField()
    country = models.CharField(max_length=50, default="India")

    
    def __str__(self):
        return self.name
    

# Create your models here