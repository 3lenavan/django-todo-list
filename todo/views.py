from django.shortcuts import render

# This function creates the page for our to-do list
def task_list(request):
    return render(request, 'todo/task_list.html')

# Create your views here.

