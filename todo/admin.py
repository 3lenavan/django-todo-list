from django.contrib import admin
from .models import Task

# Customize how tasks appear in the Django admin
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    # Columns shown in the task list
    list_display = ('title', 'completed', 'created_at')

    # Add a filter for completed tasks
    list_filter = ('completed',)

    # Allow searching by task title
    search_fields = ('title',)