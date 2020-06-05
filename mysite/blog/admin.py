from django.contrib import admin
from .models import Post

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