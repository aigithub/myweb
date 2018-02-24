from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    choice_status=(('draft','Draft'),('post','Post'),)
    title=models.CharField(max_length=250)
    slug=models.CharField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,status=choice_status,default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title





