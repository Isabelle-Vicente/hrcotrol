from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from department.models import Department
from .models import Employee
from .forms import EmployeeForm, LoginForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                employee = Employee.objects.get(email=email, password=password)
                user, created = User.objects.get_or_create(username=email, defaults={'email': email})
                auth_login(request, user)  
                return redirect('home')
            except Employee.DoesNotExist:
                messages.error(request, "Credenciais inválidas.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)  
    return redirect('login')  


@login_required
def employee_list(request):
    employee_list = Employee.objects.all()

    # Filtro por nome
    name_filter = request.GET.get('name')
    if name_filter:
        employee_list = employee_list.filter(first_name__icontains=name_filter)

    # Filtro por departamento
    department_filter = request.GET.get('department')
    if department_filter:
        employee_list = employee_list.filter(department__name__iexact=department_filter)

    # Ordenação e paginação
    employee_list = employee_list.order_by('first_name')
    paginator = Paginator(employee_list, 4)
    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)

    # Obtendo todos os departamentos
    departments = Department.objects.all()

    # Pegando o funcionário atual (logado)
    current_employee = Employee.objects.filter(email=request.user.username).first()

    return render(request, 'employees/employee_list.html', {
        'employees': employees,
        'departments': departments,
        'current_employee': current_employee  # Adicionando o funcionário atual ao contexto
    })


@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)  
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})
