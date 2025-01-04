from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from django.utils import timezone
from datetime import datetime, date
from django.db.models import Q


@login_required
def tasks(request):
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    sort_by = request.GET.get('sort_by')

    tasks = Task.objects.filter(created_by=request.user)

    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)
    
    if sort_by == 'due_date':
        tasks = tasks.order_by('due_date')
    elif sort_by == 'priority':
        tasks = tasks.order_by('priority')

    return render(request, 'task/tasks.html', {'tasks': tasks})


@login_required
def task(request, pk):
    task = Task.objects.filter(created_by=request.user).get(pk=pk)
    return render(request, 'task/task.html', {
        'task':task
    })




@login_required
def add_task(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        due_date_str = request.POST.get('due_date')

        try:
            # Parse and validate the due date
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            if due_date < date.today():
                return render(request, 'task/add.html', {
                    'error_message': "The due date cannot be in the past.",
                    'name': name,
                    'description': description,
                    'priority': priority,
                    'due_date': due_date_str,
                    'today': date.today().isoformat(),  # Add today's date to context
                })

            # Create the task with the logged-in user
            task = Task.objects.create(
                name=name,
                description=description,
                priority=priority,
                due_date=due_date,
                created_by=request.user
            )
            return redirect('/tasks/')  # Adjust URL name as needed

        except ValueError:
            return render(request, 'task/add.html', {
                'error_message': "Invalid due date format.",
                'name': name,
                'description': description,
                'priority': priority,
                'due_date': due_date_str,
                'today': date.today().isoformat(),
            })

    return render(request, 'task/add.html', {
        'today': date.today().isoformat(),  # Pass today's date for min attribute
    })




@login_required
def edit_task(request, pk):
    task = Task.objects.filter(created_by=request.user).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name','')
        description = request.POST.get('description','')
        priority = request.POST.get('priority')

        if name:
            task.name = name
            task.description = description
            task.priority = priority
            task.save()

            return redirect('task:task', pk=task.id)
        

    return render(request, 'task/edit.html', {
        'task':task
    })

@login_required
def delete_task(request, pk):
    task = Task.objects.filter(created_by=request.user).get(pk=pk)
    task.delete()

    return redirect('/tasks/')


@login_required
def complete_task(request, pk):
    task = Task.objects.filter(created_by=request.user).get(pk=pk)
    
    # Toggle the task status and update the completed_at field
    if task.status == 'completed':
        task.status = 'pending'
        task.completed_at = None  # Reset the completed_at field when it's set back to pending
    else:
        task.status = 'completed'
        task.completed_at = timezone.now()  # Set the completed_at field to the current time
    
    task.save()
    return redirect('task:task', pk=task.pk)  # Redirect to the task detail page