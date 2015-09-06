from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Post

def index(request):
    return render(request, 'apartments/index.html')

def new(request):
    context = {
        'title': 'New Posts!',
        'apartment_posts': Post.objects.filter(interesting=None).order_by('found_time')
    }
    return render(request, 'apartments/list.html', context)

def interesting(request):
    context = {
        'title': 'Interesting',
        'apartment_posts': Post.objects.filter(interesting=True).order_by('found_time')
    }
    return render(request, 'apartments/list.html', context)

def trash(request):
    context = {
        'title': 'Trash',
        'apartment_posts': Post.objects.filter(interesting=False).order_by('found_time')
    }
    return render(request, 'apartments/list.html', context)

@csrf_exempt
def update_post(request, post_id):
    if request.method == 'PUT':
        post = get_object_or_404(Post, pk=post_id)
        put = json.loads(request.body.decode("utf-8"))
        post.interesting = put.get("interesting", post.interesting)
        post.comment = put.get("comment", post.comment)
        post.save()
        return HttpResponse("Updated post: %s" % post_id)
    return HttpResponseNotAllowed(["PUT"])

def settings(request):
    return render(request, 'apartments/index.html')
