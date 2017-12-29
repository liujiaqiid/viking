from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Iaas, Zone, Server

admin.site.site_header = _("Vikings DevOps Management System")
admin.site.site_title = _("Vikings DevOps Management System")
admin.site.site_url = ""
# admin.site.index_template = 'admin/_index.html'
# admin.site.app_index_template = 'admin/_app_index.html'

admin.site.register(Iaas)
admin.site.register(Zone)
admin.site.register(Server)
