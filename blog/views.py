from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def blogview(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html',{'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Obtén el post o devuelve un error 404 si no existe
    return render(request, 'blog/post.html', {'post': post})  # Renderiza la plantilla con el post
