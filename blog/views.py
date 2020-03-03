from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home(request):
    home_context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', home_context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})