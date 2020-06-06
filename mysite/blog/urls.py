from django.urls import path
#from .models import Post
from . import views


## this app_name provide the namespace
## it helps to locate faster

app_name = 'blog'

urlpatterns = [
        #post view
        path('',views.post_list,name='post_list'),
        #path('',views.PostList.as_view(),name='post_list'),
        path('<int:year>/<int:month>/<int:day>/<slug:post>',views.post_detail,name='post_detail'),

        ## making another route for fetching postlist
        ## with tag_slug
        ## you can hit one controller with
        ## multiple routes
        ## and using optional parameter
        ## you can sort ov gain a override functionlity
        path('tag/<slug:tag_slug>/',views.post_list,name='post_list_by_tag'),
]
