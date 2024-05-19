from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from vege.views import *

urlpatterns = [
    path('login-page',login_page , name='login_page'),
    path('logout-page',logout_page , name='logout_page'),
    path('register-page',register_page , name='register_page'),
    path('delete-receipe/<int:id>', delete_receipe, name='delete_receipe'),
    path('update/<id>/', update_receipe, name='update_receipe'),
    path('update/update_link/<id>', update_link, name='update_link'),
    path('', receipes, name='receipes'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
