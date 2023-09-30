from helpers.models import TrackingModel
from django.db import models


class Todo(TrackingModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey("authentication.User", related_name="todos", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
