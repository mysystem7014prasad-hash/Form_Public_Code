
from django.db import models


class StudentDetails(models.Model):
    rollno = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    course = models.CharField(max_length=100)
    enrollment_id = models.CharField(
    max_length=8,
    unique=True,
    null=True,
    blank=True
)
    def __str__(self):
        return f"{self.rollno} - {self.name}"
