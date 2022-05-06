from django.shortcuts import render
from .models import Post, Tag, PostTag
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    posts = Post.objects.all()
    p = Paginator(posts, 4)
    page = request.GET.get('page')
    page_obj = p.get_page(page)

    return render(request, "feed.html", {
        'posts_list': posts,
        'page_obj': page_obj
    })


def get_post(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'post.html', {
        'post_obj': post
    })


def get_tags(request, tag_id):
    tags = Tag.objects.all()

    posts_list = PostTag.objects.filter(tag_id=tag_id)
    posts = []
    for post in posts_list:
        posts.append(Post.objects.filter(id=post.post_id))

    paginator = Paginator(posts, 4)  # pagination
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'feed.html', {
        'tags_list': tags,
        'page_obj': page_obj
    })
