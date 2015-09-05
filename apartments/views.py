from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict

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

@csrf_exempt
def update_post(request, post_id):
    if request.method == 'PUT':
        post = get_object_or_404(Post, pk=post_id)
        put = QueryDict(request.body)
        interest = bool(int(put.get("interesting")))
        post.interesting = interest
        post.save()
        return HttpResponse("Changed interest to %s on post %s" % (interest,
                                                                   post_id))
    return HttpResponseNotAllowed(["PUT"])

def settings(request):
    return render(request, 'apartments/index.html')
