from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_CHOICES = (
    ("draft","Draft"),
    ("published","Published"),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=270,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    body = models.TextField()
    publish = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) ## add date in the first time
    updated = models.DateTimeField(auto_now=True) ## add every time updated

    ## setting the choices
    ## and set the fefault
    ## choices are string
    ## if you add a choice parameter then
    ## your input limted with the choice
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')


    class Meta:
        ## you have to add the comma
        ordering =('-publish',)


    def __str__(self):
        return " Title : {}       Author : {}      Status: {}".format(self.title,self.author,self.status)
