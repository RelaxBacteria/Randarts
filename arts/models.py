from django.db import models
<<<<<<< HEAD
from taggit.managers import TaggableManager

from users.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='Likes', blank=True)
    caught_count = models.IntegerField()
    tags = TaggableManager()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.user) + str(self.title)

    def total_likes(self):
        return self.likes.count()

    class Meta():
        verbose_name = "게시물"
        verbose_name_plural = "게시물"

class Comment(BaseModel):
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.user) + str(self.content)
=======

# Create your models here.
>>>>>>> a0abb14f89ddca52fedf33fe1dec85686c1b26d8
