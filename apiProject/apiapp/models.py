from django.db import models


# Create your models here.
class ApiModels(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name + ', '+ self.email
    

