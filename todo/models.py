from django.db import models

class Todo(models.Model):
    todo_text = models.CharField(max_length=50)
    todo_done = models.BooleanField(default=0)

    def __str__(self):
        return self.todo_text

    def __bool__(self):
        return self.todo_done


class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    todo_comment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.todo_comment

    def __bool__(self):
        return self.todo_done
