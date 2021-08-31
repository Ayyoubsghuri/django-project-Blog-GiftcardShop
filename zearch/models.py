from django.db import models

# Create your models here.

class zearch(models.Model):
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=300, unique=True)
    
    def __str__(self):
        return self.title
    


        # http://udemydownloader.net/?s=ecommerce+and