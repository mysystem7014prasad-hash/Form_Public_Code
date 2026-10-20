
from django.contrib import admin
from .models import StudentDetails


@admin.register(StudentDetails)
class StudentDetailsAdmin(admin.ModelAdmin):

    # Columns displayed in Django Admin
    list_display = (
        "enrollment_id",
        "rollno",
        "name",
        "email",
        "phone",
        "course",
    )

    # Search students by enrollment ID and other details
    search_fields = (
        "enrollment_id",
        "rollno",
        "name",
        "email",
    )

    # Filter students by course
    list_filter = ("course",)

    # Sort students by name
    ordering = ("name",)
