from django.shortcuts import render
from .models import Post
# Create your views here.


def AllPost(request):
    posts = Post.objects.all()
    # context = {
    #     'post' : posts
    # }
    return render(request,'post/allPost.html',{'posts':posts})

def PostDetail(request,id):

    post = get_object_or_404(Post,status=Post.Status.PUBLISHED,id=Post.id)
    return render(request,'post/PostDetail.html',{'post':post})