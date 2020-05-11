from django.db import models
import uuid
# Create your models here.
class TodoStatus(models.Model):
    status_choices = (
        ('New','New'),
        ('In progress','In progress'),
        ('Completed','Completed')
    )
    status = models.CharField(max_length = 30, choices = status_choices)

    def __str__(self):
        return self.status


class Todo(models.Model):

    task_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length = 240, blank= True)
    description = models.TextField()
    labels = models.CharField(max_length = 240, blank= True)
    due_date = models.DateField()
    created_date = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False, editable=False)
    status = models.ForeignKey(TodoStatus,on_delete= models.CASCADE, related_name="todo_status", null =True)

    def __str__(self):
        return self.name



    


