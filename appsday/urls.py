"""appsday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include  # For django versions from 2.0 and up
from django.conf import settings
from onlineapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Homeview.as_view(),name="home_html"),
    path('season/<int:id>', Seasonview.as_view(), name="season_html"),
path('points/<int:id>', Pointsview.as_view(), name="points_html"),
    path('season/<int:id>/<int:pk>', Matchview.as_view(), name="match_html"),
    path('login/', loginview.as_view(),name="login_url"),
path('signup/', signupview.as_view(),name="signup_url"),
path('logout/', logout_user)
]
