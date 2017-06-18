from rest_framework import generics, response
from rest_framework import status

from api.models import Department, Employee
from api.serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentListView(generics.ListAPIView):
    """Define service to get departments list"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeCreateView(generics.ListCreateAPIView):
    """Define service to create employees."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
