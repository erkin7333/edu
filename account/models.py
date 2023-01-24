from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    image = models.ForeignKey("Image", on_delete=models.CASCADE, blank=True, null=True)




class Image(models.Model):
    image = models.ImageField(upload_to='user_image',  default="no_photo.jpg",)

    class Meta:
        verbose_name = 'User rasmi'
        verbose_name_plural = "User rasmlari"



