from django.contrib import admin

# Register your models here.

from .models import Students, Course


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'phone', 'course_name', 'is_active']
    sortable_by = ['course_name', 'is_active']
    list_filter = ['course_name', 'is_active']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name']


admin.site.register(Students, StudentsAdmin)
admin.site.register(Course, CourseAdmin)
