# employees/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Rating, Comment
from django.utils import timezone
from django.contrib import messages
from .forms import SignUpForm  # forms.py’dan import et

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    comments = Comment.objects.filter(employee=employee).order_by('-created_at')

    if request.method == "POST":
        rating_type = request.POST.get("rating")
        comment_text = request.POST.get("comment")

        if rating_type:
            Rating.objects.create(employee=employee, rating_type=rating_type)

        if comment_text:
            Comment.objects.create(employee=employee, text=comment_text)

        return redirect('employee_detail', employee_id=employee.id)

    return render(request, 'employees/employee_detail.html', {
        'employee': employee,
        'comments': comments
    })

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can log in after admin approval.')
            return redirect('login')  # login URL ismini kendi projenize göre ayarla
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
