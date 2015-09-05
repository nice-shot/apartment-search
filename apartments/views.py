from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    return render(request, 'apartments/index.html')

def new(request):
    context = {
        'title': 'New Posts!',
        'apartment_posts': Post.objects.filter(interesting=None)
    }
    return render(request, 'apartments/list.html', context)

def interesting(request):
    context = {
        'title': 'Interesting',
        'apartment_posts': Post.objects.filter(interesting=True)
    }
    return render(request, 'apartments/list.html', context)

def trash(request):
    context = {
        'title': 'Trash',
        'apartment_posts': Post.objects.filter(interesting=False)
    }
    return render(request, 'apartments/list.html', context)

def update_post_interest(request, post_id, interesting):
    post = get_object_or_404(Post, pk=post_id)
    post.interesting = bool(interesting)
    post.save()
    return HttpResponse("Changed interest to %s on post %s" % (interesting,
                                                               post_id))

def settings(request):
    return render(request, 'apartments/index.html')
