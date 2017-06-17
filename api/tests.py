from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient

from .models import Employee, Department


class TestEmployeeModel(TestCase):
    """Employee model test case."""

    client = None

    @classmethod
    def setUpClass(cls):
        super(TestEmployeeModel, cls).setUpClass()
        client = APIClient()

    def setUp(self):
        """Create departments to use in tests"""
        Department(name='Architecture').save()
        Department(name='E-commerce').save()
        Department(name='Mobile').save()

    def tearDown(self):
        """Delete departments for test."""
        Department.objects.all().delete()

    def test_model_can_add_an_employee(self):
        """Employee model test."""
        department = Department.objects.get(name='Architecture')
        employee = Employee(
            name='Arnaldo Pereira',
            email='arnaldo@luizalabs.com',
            department=department
        )
        employee.save()
        # Check if it's saved
        check_employee = Employee.objects.get(name='Arnaldo Pereira')
        self.assertIsNotNone(check_employee)

    def test_add_api_creates_employee(self):
        """Test to create an employee using the API."""
        response = self.client.post(
            reverse('add'),
            data={
                'name': 'Renato Pedigoni',
                'email': 'renato@luizalabs.com',
                'department': 'E-commerce'
            },
            format='json'
        )
        print('\n{}response: {}'.format(10 * '>', response))
        self.assertEquals(response.status_code, 201)

#    def test_serializer_can_serialize_employee_into_json(self):
#        response = self.client.post(
#            reverse('add'),
#            data={},
#            format='json'
#        )
