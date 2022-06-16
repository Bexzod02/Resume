from django.shortcuts import render,redirect,get_object_or_404
from .models import Partner, About, Resume, Projects
from main.models import Category
from main.models import Services
from main.forms import GetInTouchForm
from django.contrib import messages
from posts.models import Post, Comment, Category, Tag
from .forms import CommentForm
# Create your views here.
def person_vew(request):
    posts = Post.objects.all()
    about = About.objects.all()
    icon = Partner.objects.all()
    resumes = Resume.objects.all()
    project = Projects.objects.all()
    categories = Category.objects.all()
    service = Services.objects.all()
    query = request.GET.get('query')
    form = GetInTouchForm(request.POST or None)
    tag = request.GET.get('tag')
    cates = request.GET.get('cates')
    if cates:
        posts = posts.filter(category__category__exact=cates)
    if query:
        posts = posts.filter(title__icontains=query)
    if tag:
        posts = posts.filter(tag__tag__exact=tag)
    if form.is_valid():
        form.save() 
        messages.success(request, 'successfully send your message')
        return redirect('#contact/')
    context = {
        'about_list':about,
        'icons':icon,
        'resumes':resumes,
        'projects':project,
       ' categories':categories,
       'services':service,
       'form': form,
       'searchs':query,
       'object_list':posts
    }
    return render(request, 'index.html', context)


def single_view(request, slug):
    article = get_object_or_404(Post, slug=slug)
    last_2_articles = Post.objects.order_by('-id')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comments = Comment.objects.filter(post__slug=slug).order_by('-id')
    form = CommentForm(request.POST or None, request.FILES)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = article
        comment.save()
        return redirect(f'/single/{article.slug}#comments')
    context = {
        'last_2_articles': last_2_articles,
        'categories': categories,
        'tags': tags,
        'comments': comments,
        'object': article,
        'form':form,
    }

    return render(request, 'single.html', context)


