from django.db import models
from proj.models import XssProject
from django.contrib.auth.models import User
import django.utils.simplejson as json
# Create your models here.


class XssModel(models.Model):
	owner = models.ForeignKey(User)
	xss_projects = models.ManyToManyField(XssProject)
	is_public = models.BooleanField()
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 255)
	config_params = models.TextField() #json{param:defaultvalue}
	recv_params = models.TextField() #{number: param}
	def configparams(self):
		return json.loads(config_params)
	def recvparams(self):
		return json.loads(recv_params)
	def set_configparams(self, config_list):
		try:
#			self.config_params = json.dumps(config_list)
		except:
			pass
	def set_recvparams(self, param_list):
		try:
#			self.recv_params = json.dumps(param_list)
		except:
			pass

