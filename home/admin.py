from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import WineInfo,WineWord
admin.site.register(WineInfo)
admin.site.register(WineWord)
# @admin.Register(ViewAdmin)
# class ViewAdmin(ImportExportModelAdmin):
#     pass
