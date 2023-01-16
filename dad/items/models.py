from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Exhibition(models.Model):
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    name = models.CharField(max_length=200)
    description = models.TextField()


class MediaType(models.Model):
    MEDIA_TYPES = (
        ('AUDIO', 'Audio Files'),
        ('VIDEO', 'Video Files'),
        ('IMAGE', 'Image Files'),
        ('TEXT', 'Text Files')
    )
    description = models.TextField()
    media_type_name = models.CharField(default='IMAGE', max_length=5, choices=MEDIA_TYPES)


class Item(models.Model):
    related_to = models.ManyToManyField('self', blank=True)
    part_of = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    type_of = models.ForeignKey(MediaType, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    description = models.TextField()
    digital_copy = models.FileField(upload_to='digital_copies')


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='favorites', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='likes', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

