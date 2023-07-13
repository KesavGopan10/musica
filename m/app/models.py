from django.db import models

# Create your models here.


class music(models.Model):

    t = models.CharField (max_length=100)
    a = models.FileField (  upload_to='songs/')
    p = models.FileField (  upload_to='music/')

    

    def __str__(self):
        return self.t

    
