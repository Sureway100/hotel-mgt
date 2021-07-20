from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'David',
        'title': 'learn mathematics',
        'content': 'one',
        'date_posted': 'August 27, 2021'
    },
    {
        'author': 'Sureway',
        'title': 'learn chemistry',
        'content': 'two',
        'date_posted': 'August 17, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'ABOUT COMPANY'})
