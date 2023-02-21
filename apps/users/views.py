from django.shortcuts import render, redirect
from apps.users.models import User, Forgot_pass
from apps.movies.models import Movie, Category
from django.contrib.auth import authenticate, login
from apps.settings.models import Settings, About,Partners
from django.http.response import HttpResponse
from django.core.mail import send_mail
import random
# Create your views here.
def register(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password == confirm_password:
                try:
                    user = User.objects.create(username = username, email = email)
                    user.set_password(password)
                    user.save()
                    user = authenticate(username = username, password = password)
                    login(request, user)
                    return redirect('index')
                except:
                    return HttpResponse('Вы не зарегистрированы!')
    context = {
        'setting': setting
    }
    return render(request, 'users/register.html', context)
    
def user_login(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index') 
        except:
            return HttpResponse('Неправильный логин или пароль')
    context = {
        'setting': setting
    }
    return render(request, 'users/login.html', context)

def profile(request,id):
    categories = Category.objects.all()
    user = User.objects.get(id = id)
    if request.user != user:
        return redirect('index')
    setting = Settings.objects.latest('id')
    about = About.objects.latest('id')
    recomandations = Movie.objects.all().order_by('?')
    partner = Partners.objects.latest('id')
    if request.method == 'POST':
        if 'update' in request.POST:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            profile_image = request.FILES.get('profile_image')
            user.username = username 
            user.first_name = first_name 
            user.email = email
            user.last_name = last_name
            user.profile_image =profile_image
            user.save()
            return redirect('profile', user.id)
        if 'delete' in request.POST:
            user.delete()
            return redirect('register')
        if 'password' in request.POST:
            oldpass = request.POST.get('oldpass')
            newpass = request.POST.get('newpass')
            confirmpass = request.POST.get('confirmpass')
            if newpass == confirmpass:
                try:
                    user = User.objects.get(username = request.user.username)
                    if  user.check_password(oldpass):
                      user.set_password(newpass)
                      user.save()
                    else:
                       return HttpResponse('Неправильный пароль')
                except:
                    return HttpResponse('Пользователь не найден')
            else:
                return HttpResponse('Пароли отличаются')
        return redirect('profile',user.id)
    context = {
        'setting': setting,
        'categories': categories,
        'about': about,
        'user': user,
        'recomandations': recomandations,
        'partner': partner,
    }
    return render(request, 'users/profile.html', context)

def forgot_pass(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email = email)
            rd_num = random.randint(100000000,999999999)
            forgot_pass = Forgot_pass.objects.create( email = email, code = rd_num)
            forgot_pass.save()
            send_mail(
            #subject 
            f"Код для сброса пароля", 
            #message 
            f"Здравствуйте,код подтверждения: {rd_num}. Никому не показывайте код", 
            #from email 
            'jamankulova.ayana283@gmail.com', 
            #to email 
            [email] 
        )
            return redirect('create_password')
        except:
            return HttpResponse("Пользователя с такой почтой нету")
    context = {
            'setting' : setting,
        }
    return render(request, 'users/forgot.html', context)

def create_password(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        code = request.POST.get('code')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password: 
            try:
                forgot_pass = Forgot_pass.objects.get( code = code )
                user = User.objects.get(email = forgot_pass.email)
                user.set_password(password)
                user.save()
                forgot_pass.delete()
                return redirect('index')
            except Exception as ex:
                return HttpResponse(ex)
        else:
            return HttpResponse('Разные пароли')
    context = {
            'setting' : setting,
        }
    return render(request, 'users/create_password.html', context)