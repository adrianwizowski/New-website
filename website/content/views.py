from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from .models import About
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home(request):
    about = About.objects.all()
    return render(request, 'pc/home.html', {'about': about})

def about(request):
    about = About.objects.all()
    return render_to_response('pc/about.html', {'about': about})



def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, "pc/contact.html", {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['test@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
