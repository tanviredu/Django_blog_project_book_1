from django.contrib import admin
from .models import Post,Comment,PostLikes

##admin.site.register(Post)


## customize the models and its display

## this is a static method that force you to login
## before accessing the model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')

    ## how you ncan filet or search the post in the adminpanel
    list_filter = ('status','created','publish','author')
    search_field = ('title','body')
    ## you have to give the comma
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields =('author',) ## you can search author when posting data
    date_hierarchy = 'publish'
    ordering = ('status','publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','created','active')
    list_filter = ('active','created','updated')
    search_field = ('name','email')

@admin.register(PostLikes)
class PostLikesAdmin(admin.ModelAdmin):
    list_display = ('user','post','created',)
    list_filter = ('created',)
    search_field = ('user','post')
