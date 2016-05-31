from django.conf import settings
from django.db import models


class Group(models.Model):
    slug = models.SlugField(max_length=30, unique=True)
    about = models.TextField()

    def __str__(self):
        return self.slug


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    group = models.ForeignKey(Group)
    slug = models.SlugField(max_length=30, unique=True)
    score = models.PositiveIntegerField(default=0)
    about = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.get_username()
