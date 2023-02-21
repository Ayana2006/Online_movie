from django.urls import path 
from apps.users.views import register, user_login, profile, forgot_pass, create_password
urlpatterns = [  
    path('register/', register, name='register'),    
    path('login/', user_login, name='login'),  
    
    path('profile/<int:id>/', profile, name='profile'),
    path('forgot_pass/', forgot_pass, name='forgot_pass'),    
    path('create_password/', create_password, name='create_password'),  
]