from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_quaryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICE=(('draft','Draft'),('published','Published'),)
    title=models.CharField(max_length=250)
    slug=models.CharField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')
    # define my object manager
    objects=models.Manager()
    published=PublishedManager()
    # define post_detail url
    def get_absoulte_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])




    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title


# define comments model
class Comments(models.Model):





