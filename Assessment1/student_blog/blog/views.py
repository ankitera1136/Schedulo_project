from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def login_view(request):
    return render(request, 'blog/login.html')

def register_view(request):
    return render(request, 'blog/register.html')

def post_detail(request, slug):
    return render(request, 'blog/post_detail.html')

def post_create(request):
    return render(request, 'blog/post_form.html')

def my_posts(request):
    return render(request, 'blog/my_posts.html')

def profile(request, username):
    return render(request, 'blog/profile.html')
