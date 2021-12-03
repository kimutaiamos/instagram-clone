from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from tinymce.models import HTMLField
# from pyuploadcare.dj.models import modelsImageField
# create your models here.
class Profile(models.Model):
    prof_pic = ImageField(blank=True,)
    bio = HTMLField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)


    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls,name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile
    @classmethod
    def filter_by_id(cls ,id):
        profile = Profile.objects.filter(user = id).first()
        return profile


class Image(models.Model):
    photo = ImageField()
    image_name = models.CharField(max_length=50)
    image_caption = HTMLField(blank=True)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)



    class Meta:
        ordering =('-post_date',)

    def save_image(self):
        self.save()

    @classmethod
    def update_caption(cls,update):
        pass

    