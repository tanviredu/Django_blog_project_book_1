from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

## adding model Manager
## and add the objects to the Post
# so we can add use it


class PublishedManager(models.Manager):
    ## override the function

    def get_queryset(self):
        ## returniing the
        ## base method with the filter
        return super(PublishedManager,self).get_queryset().filter(status='published')
        ## now the get query set will always
        ## send the filter
        ## now we have to add it to the Post
        ## so we can access it













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

    # adding the object of the custom manager
    # and also the deault one
    # we need both
    # because the admin panel will use
    # the default one
    # and we use the published one
    # other wise we will see the only published post in admin admin panel
    # in admin panel we want all of it draft and published
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ## you have to add the comma
        ordering =('-publish',)


    def __str__(self):
        return " Title : {} uthor : {} Status: {}".format(self.title,self.author,self.status)

    def get_ablosute_url(self):
        ## in reverse we call the url with the name
        ## attach to it
        ## and the argument that the method in views.py
        ## that is pointed to the url
        return reverse('blog:post_detail',args = [
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])

        ## we used this

class Comment(models.Model):
    # this related name will call it
    #like post.comments
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)


    def __str__(self):
        return "Comment by {} on {}".format(self.name,self.post)
