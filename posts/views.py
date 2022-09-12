from django.shortcuts import render
from .models import Post


# Create your views here.


def single_view(request, slug):
    obj = Post.objects.get(slug=slug)
    ctx = {
        'post': obj,
    }
    return render(request, 'single.html', ctx)
