from django.shortcuts import render,HttpResponse
from .models import Department, Employee, Role
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps,
    }
    return render(request,'all_emp.html', context = context)

def add_emp(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = request.POST['role']
        phone = int(request.POST['phone'])

        new_emp = Employee(first_name = first_name, last_name = last_name, dept_id = dept, salary = salary, bonus = bonus, role_id = role, phone = phone, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("THERE is an ERROR")

def remove_emp(request, emp_id = 0):

    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("Please enter an Valid id")

    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html', context = context)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        phone = request.POST['phone']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains = name)| Q(last_name__icontains = name))

        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if phone:
            emps = emps.filter(phone = phone)

        context = {
            'emps' : emps,
        }


        return render(request,'all_emp.html', context = context)

    elif request.method == "GET":
        return render(request, 'filter_emp.html')

    else:
        return HttpResponse("An Exception occured")


