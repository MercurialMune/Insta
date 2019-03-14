from django.test import TestCase
from .models import Profile, Image
import datetime as dt


# Create your tests here.
class ImageTest(TestCase):
    def setUp(self):

        self.loc = Profile(name='Nairobi')
        self.loc.save()

        test_date = '2019-01-10'
        self.date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()

        self.img = Image(name='Awesome.jpg', category=self.cat, location=self.loc, post_date=self.date)

    def test_instance(self):
        self.assertTrue(isinstance(self.img, Image))

    def test_save_method(self):
        self.img.save_photo()
        photos = Image.objects.all()
        self.assertTrue(len(photos) > 0)

    def test_delete_image(self):
        self.img.save_photo()
        less = Image.objects.all().delete()
        self.assertTrue(len(less) < 0)

    def test_update_image(self):
        self.img.save_photo()
        photos = Image.objects.all().update()
        self.assertTrue(len(photos) > 0)

    def tearDown(self):
        Image.objects.all().delete()


class ProfileTest(TestCase):
    def setUp(self):
        self.prof = Profile(bio='love this!', pic='lol.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.prof, Profile))

    def test_save_method(self):
        self.prof.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.prof.save_profile()
        profile = Profile.objects.all().delete()
        self.assertTrue(len(profile) < 0)

    def tearDown(self):
        Profile.objects.all().delete()



