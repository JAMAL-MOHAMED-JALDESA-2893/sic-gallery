from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=30)

    def saveCategory(self):
        self.save()

    def deleteCategory(self):
        self.delete()


    @classmethod
    def updateCategory(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def __str__(self):
        return self.categoryName   


class Location(models.Model):
    locationName = models.CharField(max_length=30)

    def saveLocation(self):
        self.save()

    def deleteLocation(self):
        self.delete()

    @classmethod
    def updateLocation(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def __str__(self):
        return self.locationName



class Image(models.Model):
    imageName = models.CharField(max_length=30)
    imageDescription = models.CharField(max_length=30)
    imageLocation = models.ForeignKey(Location,on_delete = models.CASCADE)
    imageCategory = models.ForeignKey(Category,on_delete = models.CASCADE)
    image = CloudinaryField('images')        
