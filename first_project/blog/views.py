from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    { 
        'author': 'John',
        'title': 'Post1',
        'content': 'This is the first post content',
        'date_posted': 'March 28,2023'
    },

    { 
        'author': 'Tom',
        'title': 'Post2',
        'content': 'This is the second post content',
        'date_posted': 'March 29,2023'
    }
]

def home(request):
	context = {
	    'posts': posts
	}
	return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

