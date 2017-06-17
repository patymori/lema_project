from rest_framework import generics

from api.models import Employee
from api.serializers import EmployeeSerializer


class EmployeeCreateView(generics.ListCreateAPIView):
    """Define service to create employees."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        """Save employee data"""
        serializer.save()
