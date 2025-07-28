# employees/models.py
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Rating(models.Model):
    RATING_CHOICES = [
        ('best', 'best'),
        ('funny', 'funny'),
        ('creative', 'creative'),
        ('responsible', 'responsible'),
        ('lazy', 'lazy'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='ratings')
    rating_type = models.CharField(max_length=15, choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.get_rating_type_display()}"


class Comment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.employee} at {self.created_at}"
