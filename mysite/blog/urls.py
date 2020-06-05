from django.urls import path
#from .models import Post
from . import views


## this app_name provide the namespace
## it helps to locate faster 

app_name = 'blog'

urlpatterns = [
        #post view
        path('',views.post_list,name='post_list'),
        path('<int:year>/<int:month>/<int:day>/<slug:post>',views.post_detail,name='post_detail')
]
