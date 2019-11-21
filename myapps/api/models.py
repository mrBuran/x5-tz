"""Api models."""
from django.db import models
from django.conf import settings


class Application(models.Model):
    """Application which will be registered by /api/register user request."""

    name = models.CharField(max_length=200)
    key = models.CharField(max_length=40)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
