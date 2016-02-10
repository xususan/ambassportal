from django.db import models
import django.contrib.auth.models as authmodels
import os

def rename_file(instance, filename):
    ext = filename.split('.')[-1]
    filename = os.path.join(os.getcwd(), 'imgs/profiles/%s.%s' % (instance.username, ext))
    return filename
    
class User(authmodels.User):
    supervisor_id = models.CharField(max_length=30, blank=True)
    college = models.CharField(max_length=30, blank=True)
    points = models.IntegerField(blank=True)
    prof_pic = models.ImageField(upload_to=rename_file, max_length=300, blank=True)

