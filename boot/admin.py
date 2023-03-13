from django.contrib import admin

# Register your models here.

from .models import Students


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'phone', 'course']
    sortable_by = ['course']
    list_filter = ['course']


admin.site.register(Students, StudentsAdmin)
