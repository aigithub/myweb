from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
from django.http import HttpResponse
from .models import Post,Comment
from .forms import CommentForm

def index(request):
    return HttpResponse("you are at the blog index")

# def post_list(request):
#     posts=Post.objects.filter(status='published')
#     return render(request,'blog/post/list.html',{'posts':posts})

def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,
                           slug=post,
                           publish__year=year,
                           publish__month=month,
                           publish__day=day,
                           status='published')
    comments=post.post_comment.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_from = CommentForm(data=request.POST)
        if comment_from.is_valid():
            new_comment = comment_from.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_from = CommentForm()
    return render(request,
                  'blog/post/detail.html',
                  {'post':post,
                   'comments':comments,
                   'new_comment':new_comment,
                   'comment_form':comment_from})

def post_list(request):
    object_list = Post.objects.all().filter(status='published')
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',
                  {'page': page,'posts': posts})

# define post_share
from .forms import EmailPostForm
from django.core.mail import send_mail

def post_share(request,post_id):
    post=get_object_or_404(Post,id=post_id, status='published')
    sent=False
    cd=None
    if request.method == 'POST':
        form =EmailPostForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absoulte_url())
            subject='{} 推荐你阅读 "{}"'.format(cd['name'], post.title)
            message= '想要了解详细可以点击 {} \n\n{} 对此的评论是:{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,cd['email'], [cd['to']])
            sent=True
    else:
        form=EmailPostForm()
    return render(request, 'blog/post/share.html', {'post':post, 'form':form, 'sent':sent, 'cd':cd})



