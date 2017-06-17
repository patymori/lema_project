"""Serializers

Module to serialize models into JSON format.
"""
from rest_framework import serializers
from .models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Department JSON serializer"""

    class Meta:
        model = Department
        fields = ('name')


class EmployeeSerializer(serializers.ModelSerializer):
    """Employee JSON serializer"""
    department_name = DepartmentSerializer(required=True)

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department_name')

    def create(self, validated_data):
        department_name = validated_data.pop('department_name')
        department = Department.objects.create(**department_name)
        employee = Employee.objects.create(department=department, **validated_data)
