from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    # date = models.DateTimeField(default=None)
    body = models.TextField(max_length=1000)
    img_url = models.CharField(max_length=100)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self) -> str:
        return self.title


