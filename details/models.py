
from django.db import models


class StudentDetails(models.Model):
    enrollment_id = models.CharField(
        max_length=8,
        unique=True,
        null=True,
        blank=True
    )

    rollno = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.enrollment_id or 'No ID'} - {self.name}"
