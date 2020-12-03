from django.db import models

# Create your models here.
class info(models.Model):
    image=models.ImageField(upload_to='staticfiles/')