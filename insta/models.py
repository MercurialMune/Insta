from django.db import models


class Profile(models.Model):
    bio = models.TextField()
    pic = models.ImageField(upload_to='profiles/')


class Image(models.Model):
    name = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.CharField(max_length=30)
    comments = models.TextField()
    pic = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self):
        self.delete()

