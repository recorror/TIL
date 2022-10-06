from django.db import models
from django.conf import settings
# Create your models here.
class todo(models.Model):
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField()
    completed = models.BooleanField()