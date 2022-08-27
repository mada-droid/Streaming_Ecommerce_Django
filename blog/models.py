from django.db import models


class BlogPost(models.Model):
    author = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    content = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - id: {self.id}"
