from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from blog.models import BLOG
from django.utils import timezone
from blog.forms import Form

def home(request):
    query = BLOG.objects.all
    content = {'list_of_objects': query}
    return render(request, 'index.html', content)

def detail(request, id = None):
    instance = get_object_or_404(BLOG, id = id)
    content = {'title': instance.title, 'instance': instance}
    return render(request, 'blogdetail.html', content)

def delete (request, id = None):
    instance = BLOG.objects.get(id = id)
    instance.delete()
    return redirect('home')

def create(request):

    if request.method == 'POST':
        f = Form(request.POST)
        if f.is_valid():
            post = f.save(commit = False)
            post.save()
            return redirect('detail', id = post.id)
    else:
        f = Form()

    content = {'form': f}
    return render(request, 'create_post.html', content)

def edit (request, id = None):

    post = get_object_or_404(BLOG, id = id)
    if request.method == 'POST':
        f = Form(request.POST, instance = post)
        if f.is_valid():
            p = f.save(commit = False)
            p.tpublish = timezone.now()
            p.save()
            return redirect('detail', id = p.id)
    else:
        f = Form(instance = post)

    content = {'form': f}
    return render(request, 'create_post.html', content)
