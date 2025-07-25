"""
URL configuration for cursed_dating_app_be project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import get_session
from .db import signup, login, getUser, randomUser, rank
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup),
    path('login/', login),
    path('getuser/', getUser),
    path('random/', randomUser),
    path('rank/', rank),
    path('accounts/', include('allauth.urls')),
    path('api/get-session', get_session, name='get_session')
]
