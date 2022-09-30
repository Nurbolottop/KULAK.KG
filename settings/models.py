from distutils.command.upload import upload
from typing import ChainMap
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Setting(models.Model):
    name_site = models.CharField(max_length = 255)
    discription_site  =models.CharField(max_length = 255)
    logo_site = models.ImageField(upload_to = 'logo/')
    facebook_site = models.URLField()
    twitter_site = models.URLField()
    instagram_site = models.URLField()
    youtube_site = models.URLField()
