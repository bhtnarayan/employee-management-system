from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Employee
from django.contrib import messages

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from . forms import EmployeeForm



@login_required(login_url = "/accounts/login/")
def create_employee(request):
    user = request.user 
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.save(commit=False) 
            data.user = user 
            data.save() 
            messages.success(request, f'Customer Created Successfully') 
            return redirect("/employee_list")
    else:
        form = EmployeeForm() 

    context = {
        'form':form,
    }
    return render(request, "main/index.html", context)

@login_required(login_url = "/accounts/login/")
def list_employee(request):
    all_employee = Employee.objects.filter(user = request.user)
    number = all_employee.count() 
    context = {
        'all_employee': all_employee,
        'number': number,
    }
    return render(request, "main/employee_list.html", context) 

@login_required(login_url = "/accounts/login/")
def detail_employee(request, pk):
    employee = Employee.objects.get(pk = pk) 
    context = {
        
        'employee': employee,
        
    }
    return render(request, "main/employee_detail.html", context) 

@login_required(login_url = "/accounts/login/")
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk = pk) 
    # for image post handling request.files
    form = EmployeeForm(request.POST or None, request.FILES or None, instance = employee) 
    if form.is_valid():
        form.save() 
        return redirect('/employee_list') 
    
    context = {
        'form': form,
    }
    return render(request, "main/index.html", context) 

@login_required(login_url = "/accounts/login/")
def delete_employee(request, pk):
    customer = get_object_or_404(Employee, pk = pk) 
    if request.method == "POST":
        customer.delete() 
        return redirect("/employee_list") 
    
    context = {

    }

    return render(request, "main/employee_delete.html", context) 

