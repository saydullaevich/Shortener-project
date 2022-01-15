from django.db import models
from .utils import shorted_url

class Shortener(models.Model):
    created = models.DateTimeField(auto_now_add=True)  
    url_first = models.URLField()
    url_second = models.CharField(max_length=15, unique=True, blank=True)
    
    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.url_first} to {self.url_second}'

    def save(self, *args, **kwargs):
        if not self.url_second:
            self.url_second = shorted_url(self)

        super().save(*args, **kwargs)