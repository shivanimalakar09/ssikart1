from distutils.command.upload import upload
from pydoc import describe
from django.db import models

# Create your models here.
class category(models.modeel):
    name=models.charfield(max_lenght=100, unique=True)
    slug=models.Charfield(max_length=100, unique=True)
    description = models.Textfield(max_lenght=255, blank=True)
    image = ImageField(upload_to='images/categories',blank=True)
    
    def __str__(self):
        return self.name
    
