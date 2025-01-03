from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task



@login_required
def tasks(request):
    tasks = Task.objects.filter(created_by=request.user)
    return render(request, 'task/tasks.html', {
        'tasks':tasks
    })

@login_required
def add_task(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        description = request.POST.get('description','')

        if name:
            Task.objects.create(name=name, description=description, created_by = request.user)

            return redirect('/tasks')
        else:
            print('Not Valid')

    return render(request, 'task/add.html')