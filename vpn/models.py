from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class UserSite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name


class SiteVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(UserSite, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    data_sent = models.PositiveIntegerField(default=0)
    data_received = models.PositiveIntegerField(default=0)