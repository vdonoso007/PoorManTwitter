from django.db import models

# Create your models here.
class Tweets(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_at', 'name')