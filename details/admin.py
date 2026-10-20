
from django.contrib import admin
from .models import StudentDetails


@admin.register(StudentDetails)
class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = ("rollno", "name", "email", "phone", "course")
    search_fields = ("rollno", "name", "email")
    list_filter = ("course",)
