from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=100)  # Rename this field to 'name'
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
