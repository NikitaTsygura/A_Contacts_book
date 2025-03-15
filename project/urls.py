"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views  # Импортируй views из твоего приложения "app"
from django.conf import settings
from django.conf.urls.static import static
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name='base'),# Маршрут для главной страницы
    path('', views.contact_list, name='contact_list'),
    path("add/", views.add_contact, name="add_contact"),
    path('', views.base, name='home'),  # главная страница
    path('new_contact/', views.new_contact, name='new_contact'),
    # path('about/<int:contact_id>/', views.about_contact, name='about_contact_detail'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
