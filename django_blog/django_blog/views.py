from django.http import HttpResponse
from django.shortcuts import render 
from posts.models import Post

def homepage(request):
    # return HttpResponse("Hello this is the homepage")
    posts = Post.objects.all()
    return render(request, 'homepage.html', {'posts': posts})

def about(request):
    # return HttpResponse("This is the about page")
    return render(request, 'about.html')