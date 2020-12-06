from django.shortcuts import render
from . import urls

# Create your views here.
def home(request):
    url = urls.urlpatterns
    return render(request, 'home/index.html', {
        'urls': url
    })