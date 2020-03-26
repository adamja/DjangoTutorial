from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # If the user is deleted the profile will be deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):  # override the save model to add functionality
        super().save()  # run the parent save method first

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
