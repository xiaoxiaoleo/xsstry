from django.contrib import admin
from proj.models import XssProject, XssItem

# Register your models here.

admin.site.register(XssProject)
admin.site.register(XssItem)
