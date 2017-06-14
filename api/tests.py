from django.test import TestCase
from .models import Employee, Department


class TestEmployeeModel(TestCase):
    """Employee model test case."""

    def setUp(self):
        Department(name='Architecture').save()
        Department(name='E-commerce').save()
        Department(name='Mobile').save()

    def tearDown(self):
        Department.objects.all().delete()

    def test_model_can_create_an_employee(self):
        department = Department.objects.get(name='Architecture')
        employee = Employee(
            name='Arnaldo Pereira',
            email='arnaldo@luizalabs.com',
            department=department
        )
        employee.save()
        check_employee = Employee.objects.get(name='Arnaldo Pereira')
        self.assertIsNotNone(check_employee)
