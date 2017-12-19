from django.contrib import admin
from .models import Iaas, Zone, Server

admin.site.register(Iaas)
admin.site.register(Zone)
admin.site.register(Server)
