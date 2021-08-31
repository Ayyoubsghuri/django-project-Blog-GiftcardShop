from django.db import models
from django.contrib.auth import get_user_model

# from djangotoolbox.fields import ListField

User =get_user_model()

# Create your models here.
class shopp(models.Model):
    title = models.CharField(max_length=200, unique=False)
    acc = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    @property
    def listacc(self,*args,**kwargs):
        z =[]
        a=self.acc.split("\n")
        for i in a:  
            z.append(i.replace("\r"," "))      
        return z

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-updated_on']

class shoporder(models.Model):
    title = models.CharField(max_length=200, unique=False)
    user =models.ForeignKey(User, 
    on_delete=models.CASCADE,related_name="timesheet",null="True")
    # quantity = models.CharField(max_length=200)
    acc = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    # categories = ListField()

    def __str__(self):
        return self.acc
    
    class Meta:
        ordering = ['-updated_on']



