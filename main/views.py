from django.shortcuts import render, redirect
from person.models import About, Partner, Resume
from posts.models import Post


# Create your views here.


def home_view(request):
    obj = About.objects.order_by('-id')[:1]
    partner = Partner.objects.all()
    post = Post.objects.order_by('-id')
    resumes = Resume.objects.all()
    q = request.GET.get('search')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    if cat:
        post = post.filter(category__category__exact=cat)
    if q:
        post = post.filter(title__icontains=q)
    if tag:
        post = post.filter(tag__tag__exact=tag)
    ctx = {
        'objects': obj,
        'partners': partner,
        'posts': post,
        'resumes':resumes
    }
    return render(request, 'index.html', ctx)

