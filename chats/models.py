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