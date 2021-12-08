from django.test import TestCase
from .models import Location,Image,image

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nairobi= Location(first_name = 'Nairobi')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
     # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images =Image.objects.all()
        self.assertTrue(len(images) > 0)

 

class ImagesTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image= image(name = 'image')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,image))

     # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        imagess = image.objects.all()
        self.assertTrue(len(categories) > 0)

    def delete_save_method(self):
        self.image.save_image()
        categories = image.objects.all()
        self.assertTrue(len(categories) == 0)


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        moringa = Image(first_name='moringa')
        moringa.save()
        image= Image(name = 'image')
        image.save()

        self.image= Image(image = 'jpg', image_name= 'image', image_description= 'hotels', image_location= moringa,image_image=image)
        self.image.save()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

     # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


    def delete_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)


    def tearDown(self):
        Location.objects.all().delete()
        image.objects.all().delete()
        Image.objects.all().delete()

    def test_retrieve_all_images(self):
        images = Image.objects.all()
        self.assertTrue(len(images) ==1)

class ModalTestClass(TestCase):
    def setUp(self):
        self.image = image(image = 'image_name')

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

     # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)