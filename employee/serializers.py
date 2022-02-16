from employee.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    manager_id = serializers.IntegerField(source='manager.id', read_only=True)
    
    class Meta:
        model = Employee
        fields = [ 'id', 'name', 'title', 'manager_id']