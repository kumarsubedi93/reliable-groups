from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=200, verbose_name='Position')
    photo = models.ImageField(upload_to='teams/', null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    fb_link = models.URLField(null=True, blank=True, verbose_name='Facebook Link')
    twitter_link = models.URLField(null=True, blank=True, verbose_name='Twitter Link')
    instagram_link = models.URLField(null=True, blank=True, verbose_name='Instagram Link')
    linked_in_link = models.URLField(null=True, blank=True, verbose_name='Linkedin Link')


    def __str__(self) -> str:
        return self.name
    

    def photo_url(self):
        if self.photo:
            return self.photo.url
        return ''


class Feedback(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
       return '{} {}'.format(self.name, self.email)
