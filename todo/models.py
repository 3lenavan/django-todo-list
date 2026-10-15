from django.db import models

# Create a Task model for each to-do item
class Task(models.Model):

    # Stores the name/title of the task
    # The title can be up to 200 characters long
    title = models.CharField(max_length=200)

    # Stores whether the task is finished
    # False means not completed yet
    completed = models.BooleanField(default=False)

    # Controls how the task is displayed
    # It will show the task's title
    def __str__(self):
        return self.title
    
# Create your models here.
