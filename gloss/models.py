from django.db import models
from django.utils import timezone


class Glossary(models.Model):
    creator = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    
    class Meta:
        verbose_name_plural = 'glossaries'

    def __str__(self):
        return self.title