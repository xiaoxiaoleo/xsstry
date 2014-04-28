from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
# Create your models here.


class Note(models.Model):
  owner = models.ForeignKey(User)
  title = models.CharField(max_length = 100)
  description = models.CharField(max_length = 255)
  context = models.TextField()
