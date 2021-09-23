from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name='Description', blank=True)
    important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    timecompleted = models.DateTimeField(null=True, blank=True, verbose_name='The time when it was completed')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Titles'
        ordering = ['created']

    def __str__(self):
        return self.title

