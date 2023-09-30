from django.db import models

class TrackingModel(models.Model): #this is an abstract model for tracking the creation and update of models
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
        ordering = ['-created_at']