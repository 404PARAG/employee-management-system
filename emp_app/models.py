from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} is at {self.location}"

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} is the role name"

class Employee(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete= models.CASCADE)
    phone = models.IntegerField(default=0000000000)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} is the employee"