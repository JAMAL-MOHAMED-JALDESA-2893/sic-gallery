from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=30)