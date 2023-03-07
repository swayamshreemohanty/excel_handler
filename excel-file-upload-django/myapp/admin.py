from django.contrib import admin
from myapp.models import Data

# Register your models here.
from import_export.admin import ImportExportActionModelAdmin
# @admin.register(Data)

class DataAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display=('application','valuation','budget')

admin.site.register(Data,DataAdmin)