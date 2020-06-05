from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from  .models import Post




class PostList(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'




# ## this is the list view
# def post_list(request):
#
#     ## get all the published post
#     object_list = Post.published.all()
#     paginator = Paginator(object_list,3)  ## 3 post in each page
#     # page automatically holds the current page number
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page);
#     except PageNotAnInteger:
#             # if now an intger show the first page
#         posts = paginator.page(1)
#
#             # else show the last page
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#
#     #return HttpResponse(posts)
#     return render(request,'blog/post/list.html',{'page':page,'posts':posts})
#

## here post parameter is the slug
def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug = post,status='published',publish__year=year,publish__month = month,publish__day=day)
    #return HttpResponse(post)
    return render(request,'blog/post/detail.html',{'post':post})
