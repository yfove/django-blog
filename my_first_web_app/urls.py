from random import randint
from django.http  import HttpResponse
from django.shortcuts import render
from django.urls import path

def home_page(request):
    context = {'name': 'John Smith'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def portfolio(request):
    random_number = randint(0,100)
    image_url = "https://picsum.photos/400/600/?image={}".format(random_number)
    context = {'gallery_image': image_url}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me(request):
    content = {
        'skills': ['ruby on rails', 'python', 'sql', 'javascript'],
        'interests': ['web development', 'software development', 'ux design']
    }
    response = render(request,'about_me.html', content)
    return HttpResponse(response)

urlpatterns = [
    path('home/', home_page),
    path('portfolio/', portfolio),
    path('about_me/', about_me),
]
