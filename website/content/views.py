from django.shortcuts import render, render_to_response
from .models import About

# Create your views here.
def home(request):
    return render(request, 'pc/home.html')

def about(request):
    about = About.objects.all()
    return render_to_response('pc/about.html', {'about': about})