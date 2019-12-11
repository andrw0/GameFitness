"""gamefitnessweb URL Configuration

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

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('signin/', views.showUserForm.as_view(), name='signin'),
    path('admin/', admin.site.urls),
    path('accounts/profile/',views.showGameForm, name='games'),
    path('exercisesList/',views.showExercisesForm, name='exercisesList'),
    path('homepage/',views.homepage, name='homepage'),
    path('feedback/', views.showFeedbackForm, name='feedback'),
    path('login/', LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'),
]
