from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
import django.utils.simplejson as json
# Create your models here.

class XssProject(models.Model):
  owner = models.ForeignKey(User)
  name = models.CharField(max_length = 50)
  description = models.CharField(max_length = 255)
  create_date = models.DateTimeField("Creating date")
  addition_code = models.TextField()
  config_params_setting = models.TextField() #json{param: value}
  def configparam(self):
    return json.loads(self.config_params_setting)

class XssItem(models.Model):
  xss_project = models.ForeignKey(XssProject)
  recv_date = models.DateTimeField("Receiving date")
  data = models.TextField() #json{name: detail}
  def itemdetail(self):
    return json.loads(self.data)
