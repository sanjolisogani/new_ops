from django.db import models

# Create your models here.
class Registered(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self):
        return str(self.email)