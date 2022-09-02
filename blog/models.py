from django.contrib.auth.models import User
from django.db import models

# from blog.mixin import CreateMixin


# class AuthorProfile(models.Model):
#     user = models.OneToOneField(User, related_name='author_profile', on_delete=models.CASCADE)
#     short_bio = models.TextField()


# class BlogPost(CreateMixin, models.Model):
class BlogPost(models.Model):
    # LA PROTECT FA SI CHE NON SI PUò ELIMINARE L'AUTORE FINCHE NE HA DEI POST,
    # IL CHE SIGNIFICA VANNO ELIMINATI PRIMA I POST ASSOCIATI POI L'AUTORE STESSO
    # author = models.ForeignKey(AuthorProfile, related_name='blog_posts', on_delete=models.PROTECT)
    author = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    content = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - id: {self.id}"
