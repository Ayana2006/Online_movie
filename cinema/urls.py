from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.settings.urls')),
    path('movie/', include('apps.movies.urls')),
    path('users/', include('apps.users.urls')),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),  
    path('log_in/', LogoutView.as_view(next_page='login'), name='log_in'),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#577713861841-8n8qg2h0g61i5uabck7amfies49v1h7c.apps.googleusercontent.com
#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