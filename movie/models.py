from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length= 50)
    short_description = models.CharField(max_length= 50)
    image = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.title}"