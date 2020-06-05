from django.shortcuts import render,HttpResponse
from django.shortcuts import get_list_or_404
from  .models import Post





## this is the list view
def post_list(request):

    ## get all the published post
    posts = Post.published.all()
    return HttpResponse(posts)
    #return render(request,'blog/post/list.html',{'posts':posts})


## here post parameter is the slug
def post_detail(request,year,month,day,post):
    post = get_list_or_404(Post,slug = post,status='published',publish__year=year,publish__month = month,publish__day=day)
    return HttpResponse(post)
    #return render(request,'blog/post/detail.html')
