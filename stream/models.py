from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from datetime import timedelta


from django.db.models.signals import post_delete
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Video(models.Model):
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, related_name='videos')
    title = models.CharField(max_length=120)
    url = models.CharField(max_length=120, blank=False)
    preview = models.ImageField(upload_to='images/',blank=True,null=True)
    description = models.TextField(blank=True)
    duration = models.DurationField(default=timedelta())
    available = models.BooleanField(default=True)
    created = models.DateTimeField(verbose_name='added', default=timezone.now)
    views = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

# delelte file with objects
@receiver(post_delete, sender=Video)
def submission_delete(sender, instance, **kwargs):
    instance.preview.delete(False) 
