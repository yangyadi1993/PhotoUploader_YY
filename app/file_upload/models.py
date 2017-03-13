from django.db import models
import os

# Create your models here.
class Picture(models.Model):
    picture = models.ImageField(upload_to="photos")

    def filename(self):
        return os.path.basename(self.picture.name)