from django.test import TestCase
from .models import Image, Category, Location


# Create your tests here.
class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='kinoo')
        self.location.saveLocation()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.saveLocation()
        locations = Location.getLocations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.location.saveLocation()
        locations = Location.getLocations()
        self.assertTrue(len(locations) > 1)

    def test_delete_location(self):
        self.location.deleteLocation()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)