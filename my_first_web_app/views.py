from random import randint
from django.http  import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request): #Redirects to http://localhost:8000/home/
    return HttpResponseRedirect('/home')

def gallery(request): #Redirects to http://localhost:8000/portfolio/
    return HttpResponseRedirect('portfolio')

def home_page(request): #Redirects to http://localhost:8000/home/
    context = {'name': 'John Smith'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def portfolio(request): #Redirects to http://localhost:8000/portfolio/
    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))

    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me(request): # http://localhost:8000/about_me/
    context = {'skills':['coding', 'design', 'photography'], 'interests':['techlead', 'silicon valley', 'ux']}

    response = render(request, 'about_me.html', context)
    return HttpResponse(response)

def favourites(request): # http://localhost:8000/favourites/
    context = {'fav_links':['https://www.freecodecamp.org/', 'https://www.10bestdesign.com/dirtymarkup/', 'https://css-tricks.com/snippets/css/a-guide-to-flexbox/', 'https://css-tricks.com/snippets/css/complete-guide-grid/']}

    response = render(request, 'favourites.html', context)
    return HttpResponse(response)