from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
