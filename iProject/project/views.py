from django.shortcuts import render, HttpResponse
from project.models import Post

# Create your views here.
def projectHome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "project/projectHome.html", context)

def projectPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "project/projectPost.html", context)

    
  
