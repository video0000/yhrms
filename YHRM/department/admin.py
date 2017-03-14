from django.contrib import admin
from django.core.handlers.wsgi import logger

from .models import Department
from simple_history.admin import SimpleHistoryAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
        import_id_fields = ('department_number',)


# Register your models here.



class DepartmentAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ('department_number', 'name', 'type', 'address', 'parent_structure')
    list_filter = ('type', 'parent_structure')
    search_fields = ['department_number', 'name']
    raw_id_fields = ['parent_structure', ]
    resource_class = DepartmentResource


admin.site.register(Department, DepartmentAdmin)
