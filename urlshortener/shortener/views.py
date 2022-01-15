from django.shortcuts import render
from django.shortcuts import render # We will use it later

from django.http import HttpResponse, Http404, HttpResponseRedirect


# Model
from .models import Shortener

# Custom form

from .forms import ShortenerForm

# Create your views here.

def home_view(request):
    
    template = 'urlshortener/home.html'

    
    context = {}

    # Empty form
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            
            shortened_object = used_form.save()

            new_url = request.build_absolute_uri('/') + shortened_object.url_second
            
            url_first = shortened_object.url_first 
             
            context['new_url']  = new_url
            context['url_first'] = url_first
             
            return render(request, template, context)

        context['errors'] = used_form.errors

        return render(request, template, context)

def redirect_url_view(request, shortened_part):

    try:
        shortener = Shortener.objects.get(url_second=shortened_part)
        
        return HttpResponseRedirect(shortener.url_first)
        
    except:
        raise Http404('Kechirasiz, bu havola buzilgan :(')