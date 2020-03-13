from django.shortcuts import render

posts = [
    {
        'author': 'Adam Jacob',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 3, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Seconds post content',
        'date_posted': 'March 5, 2020'
    },
]


def home(request):
    context = {
        'title': 'Home',
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'blog/about.html', context)
