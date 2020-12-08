from django.db import models

class gallery_details(models.Model):
    gallery_category= models.CharField(max_length=100)
    img = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.gallery_category