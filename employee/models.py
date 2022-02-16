from django.db import models

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        manager = f"| Manager: {self.manager.name}" if self.manager else ""
        return f"ID[{self.id}]: {self.name} ({self.title}) {manager}"
