from django.contrib import admin
from congresvoorstel.voorstel.models import *


class AmendementAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'email']
    list_filter = ['status']

admin.site.register(Amendement, AmendementAdmin)
admin.site.register(AmendementComment)

