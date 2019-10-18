# from random import randint
# from django.http  import HttpResponse
# from django.shortcuts import render
# from django.urls import path

# def home_page(request):
#     context = {'name': 'John Smith'}
#     response = render(request, 'index.html', context)
#     return HttpResponse(response)

# def portfolio(request):
#     random_number = randint(0,100)
#     image_url = "https://picsum.photos/400/600/?image={}".format(random_number)
#     context = {'gallery_image': image_url}
#     response = render(request, 'gallery.html', context)
#     return HttpResponse(response)

# def about_me(request):
#     content = {
#         'skills': ['ruby on rails', 'python', 'sql', 'javascript'],
#         'interests': ['web development', 'software development', 'ux design']
#     }
#     response = render(request,'about_me.html', content)
#     return HttpResponse(response)

# def favourites(request):
#     fave_links_list = ['']
#     context = {'fave_links': fave_links_list}
#     response = render(request,'favourites.html', context)
#     return HttpResponse(response)
from django.urls import path
from my_first_web_app.views import root, gallery, home_page, portfolio, about_me, favourites

urlpatterns = [
    path('', root), #Redirect
    path('gallery/', gallery), #Redirect
    path('home/', home_page), #Page
    path('portfolio/', portfolio), #Page
    path('about_me/', about_me), #Page
    path('favourites/', favourites), #Page
]