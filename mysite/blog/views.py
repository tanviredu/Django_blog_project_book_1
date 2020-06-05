from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from  .models import Post
from  .forms import CommentForm




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

    ## getting all the comments
    comments = post.comments.filter(active=True)

    ## setting new comment status
    new_comment = None

    if request.method == 'POST':
        ## comment is taken from the
        ## form class
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():

            ## make the object for saving
            ## but not doing it right now
            new_comment = comment_form.save(commit=False)
            # now we need to add the Post
            ## to the current object
            ## so we will know which commnt is for
            ## which post
            #because in the form we do not provide the
            # filed and we should not
            new_comment.post = post

            # now save
            new_comment.save()
    else:
        # if there is no comment
        # then give them the form
        comment_form = CommentForm()
        #and render it
        return render(request,'blog/post/detail.html',{'post':post,'comments':comments,'new_comment':new_comment,'comment_form':comment_form})
