from django.contrib import admin
from employee.models import Employee

# Register your models here.
# admin.site.register(Employee)


from import_export.admin import ImportExportActionModelAdmin

@admin.register(Employee)
class usrdet(ImportExportActionModelAdmin):
    pass


# class DataAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
#     list_display=('eid','application','valuation','budget')

# admin.site.register(Employee,DataAdmin)