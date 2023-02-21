from django.shortcuts import render, redirect
from apps.settings.models import Settings, Privacy, About, Partners, Contact
from apps.movies.models import Category, Movie
from django.core.mail import send_mail
# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    categories = Category.objects.all()
    movies = Movie.objects.all().order_by('year')
    context = {
        'setting':setting,
        'movies':movies, 
        'categories':categories,
    }
    return render(request, 'settings/index.html', context)

def privacy(request):
    setting = Settings.objects.latest('id')
    privacy = Privacy.objects.latest('id')
    context = {
        'setting' : setting,
        'privacy' : privacy
    }
    return render(request, 'settings/privacy.html', context)

def about(request):
    setting = Settings.objects.latest('id')
    about = About.objects.latest('id')
    partner = Partners.objects.latest('id')
    context = {
        'setting' : setting,
        'about' : about,
        'partner' : partner,
    }
    return render(request, 'settings/about.html', context)

def contacts(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        otklic = Contact.objects.create(name = name, email = email,subject = subject, text = message, phone=phone)
        otklic.save()
        send_mail(
            #subject 
            f"Спасибо за отклик: {subject}", 
            #message 
            f"Здравствуйте {name}, спасибо за отклик мы с вами свяжемся. Ваше сообщение: {message}, ваш номер: {phone}", 
            #from email 
            'jamankulova.ayana283@gmail.com', 
            #to email 
            [email] 
        )
        return redirect('index')
    context = {
        'setting' : setting,
    }
    return render (request, 'settings/contacts.html', context)

