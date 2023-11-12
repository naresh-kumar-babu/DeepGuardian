from django.db import models

class ImagePicker(models.Model):
    image = models.ImageField(default="input_img.jpg")

    def get_url(self):
        return self.image.url

class VideoPicker(models.Model):
    video = models.FileField(default="input_video.mp4")

    def get_url(self): 
        return self.video.url   