from django.shortcuts import render, redirect
from .models import Task

# This function displays the to-do list page
def task_list(request):

    # Check if the user submitted the form
    if request.method == 'POST':

        # Get the task title from the form
        title = request.POST.get('title')

        # Create a new task if the title is not empty
        if title:
            Task.objects.create(title=title)

        # Reload the page after adding the task
        return redirect('task_list')

    # Get all tasks from the database
    tasks = Task.objects.all().order_by('-created_at')

    # Send the tasks to the HTML page
    return render(request, 'todo/task_list.html', {'tasks': tasks})

    # This function marks a task as completed
def complete_task(request, task_id):

    # Find the task using its ID
    task = Task.objects.get(id=task_id)

    # Mark the task as completed
    task.completed = not task.completed

    # Save the change to the database
    task.save()

    # Go back to the to-do list page
    return redirect('task_list')

    # This function deletes a task
def delete_task(request, task_id):

    # Find the task using its ID
    task = Task.objects.get(id=task_id)

    # Delete the task from the database
    task.delete()

    # Go back to the to-do list page
    return redirect('task_list')