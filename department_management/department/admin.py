# department/admin.py

from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'status')
    search_fields = ('dept_name',)
