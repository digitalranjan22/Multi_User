from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# from crm.accounts.decorators import unauthenticated_user

from .decorators import unauthenticated_user , allowed_users , admin_only

# from crm.accounts.models import Products
from .models import Employee, Order, Products
from .forms import CreateUserForm

# @login_required(login_url='login/')
@unauthenticated_user
def registerPage(request):
   
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Account Was  Created for '+ username)
            return redirect('login')

    context = { 'form':form}
    return render(request,'accounts/register.html',context)
@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username or password is incorrect')
            # return render(request,'accounts/login.html',context)
    context = { }
    return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def userPage(request):
    context = {}
    return render(request,'accounts/user.html',context)


@login_required(login_url='login/')
@admin_only
def home(request):
    employees = Employee.objects.all()
    orders = Order.objects.all()

    # total_employees = employees.count()
    # total_orders = order.
    context ={'orders' : orders, 'employees':employees}
    return render(request ,'accounts/dashboard.html',context)

@login_required(login_url='login/')
@allowed_users(allowed_roles=['admin'])
def product(request):
    product = Products.objects.all()
    return render(request ,'accounts/products.html',{'product':product})

@login_required(login_url='login/')
@allowed_users(allowed_roles=['admin'])
def customer(request):
    return render(request ,'accounts/customer.html')

