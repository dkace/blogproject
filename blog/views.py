from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category
import markdown
from comments.forms import CommentForm

# Create your views here.

def index(request):
    # return render(request,'blog/index.html',context={
    #     'title':'DK视界',
    #     'welcome':'欢迎访问我的博客首页！',
    #     'dir':'曾经有一段真挚的爱情，我要好好珍惜！'
    # })
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list': post_list})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc'
                                  ])
    form = CommentForm()
    comment_list = post.comments_set.all()
    context = {'post':post,
                'form':form,
               'comment_list':comment_list
    }
    # return render(request,'blog/detail.html',context={'post':post})
    return render(request,'blog/detail.html',context=context)


def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})