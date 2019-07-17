from django.db import models

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Meeting(models.Model):
    title = models.CharField(max_length=100)    
    obj = models.CharField(max_length=100, blank=True)    
    points = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    members = models.ManyToManyField(User, related_name='meetings', blank=True)
    chairperson = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    begin = models.TimeField(auto_now_add=True)
    end = models.TimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now=True, blank=True)
    previous_meeting = models.OneToOneField('self', on_delete=models.SET_NULL, blank=True, related_name='previous', null=True)
    next_meeting = models.OneToOneField('self', on_delete=models.SET_NULL, blank=True, related_name='next', null=True)

    def __str__(self):
        return self.title


class Transcription(models.Model):
    author = models.ForeignKey(User, related_name='transcriptions', on_delete=models.CASCADE, blank=True, null=True)
    meeting = models.ForeignKey(Meeting, related_name='transcriptions', on_delete=models.CASCADE, blank=True)

    info = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.info


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info')
    photo = models.ImageField()
    job = models.CharField(max_length=100)
    phone = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.user.username + "_profile"
