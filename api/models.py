from django.db import models
import uuid


class Todo(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=120, unique=True, verbose_name="Name")
  pub_date = models.DateTimeField()

  def __str__(self):
    return self.name

class Task(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=120, unique=True, verbose_name="Name")
  todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
  pub_date = models.DateTimeField()

  def __str__(self):
    return self.name
