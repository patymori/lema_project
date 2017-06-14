from django.db import models

class Department(models.Model):
    """Department model class."""
    name = models.CharField(max_length=30, blank=False, unique=True)

    def __str__(self):
        return '{}'.format(self.name)

class Employee(models.Model):
    """Employee model class."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    email = models.EmailField(blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ('name',)
