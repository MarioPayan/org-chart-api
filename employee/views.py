from rest_framework import viewsets
from employee.serializers import EmployeeSerializer
from employee.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
