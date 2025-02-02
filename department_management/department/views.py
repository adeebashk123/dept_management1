# department/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Department
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def dashboard(request):
    departments = Department.objects.all()  # Get all departments
    query = request.GET.get('q')
    if query:
        departments = departments.filter(dept_name__icontains=query)  # Filter based on department name
    
    return render(request, 'dashboard.html', {'departments': departments})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("dashboard")  # Redirect to the dashboard after login
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")

def home(request):
    return render(request, "home.html")

def add_department(request):
    if request.method == 'POST':
        dept_name = request.POST.get('dept_name')
        description = request.POST.get('description')

        # Check if dept_name is empty
        if not dept_name:
            messages.error(request, "Department name cannot be empty.")
            return redirect('add_department')  # Correct the redirect

        if Department.objects.filter(dept_name=dept_name).exists():
            messages.error(request, "Department already exists.")
        else:
            Department.objects.create(dept_name=dept_name, description=description)
            messages.success(request, "Department added successfully.")

        return redirect('dashboard')  # Redirect to dashboard after adding department

    return render(request, 'add_department.html')  # Render the form to add department



from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from django.contrib import messages

def modify_department(request, department_id):
    # Get the department object
    department = get_object_or_404(Department, id=department_id)
    
    if request.method == 'POST':
        # Retrieve the updated department name and description from the form
        dept_name = request.POST.get('dept_name')
        description = request.POST.get('description')
        
        # Update the department fields
        department.dept_name = dept_name
        department.description = description
        department.save()  # Save the changes to the database
        
        # Show success message
        messages.success(request, "Department updated successfully.")
        return redirect('dashboard')  # Redirect back to the dashboard
    
    # Render the form for GET requests (when initially visiting the page)
    return render(request, 'modify_department.html', {'department': department})

def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == 'POST':
        if department.status:
            messages.error(request, "Please reassign employees linked to this department before deletion.")
        else:
            department.status = False
            department.save()
            messages.success(request, "Department deactivated successfully.")
        return redirect('dashboard')
    return render(request, 'delete_department.html', {'department': department})
