from django.db import models
from froala_editor.fields import FroalaField
from decimal import Decimal


STATUS = (
    ("CPA", "CPA"),
    ("ECOMMERCE", "ECOMMERCE"),
    ("DROPSHIPPING", "DROPSHIPPING"),
    ("RISKING", "RISKING"),
    ("SCRIPTS", "SCRIPTS"),
    ("AUTO", "AUTO"),
)
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    thumb = models.ImageField(upload_to='photos/%y/%d', default='profile.jpg')
    # active=models.models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=16, choices=STATUS)
    content = FroalaField(blank=True, null=True)
    intro = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class PostVIP(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    thumb = models.ImageField(upload_to='static/photos/%y/%m/%d', default='profile.jpg')
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=16, choices=STATUS)
    content = FroalaField(blank=True, null=True)
    intro = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
