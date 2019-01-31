"""work_bgm_club URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
# from work_bgm_club import views

from rest_framework import routers
from musiclink.viewsets import MusicLinkViewSet, MusicRatingViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'musiclinks', MusicLinkViewSet)
router.register(r'musicrating', MusicRatingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('api/public/', views.public),
    # path('api/private/', views.private),
    path('accounts/', include('allauth.urls')),
    path('privacy_policy/', TemplateView.as_view(template_name='privacy_policy.html')),
    path('termsofservice/', TemplateView.as_view(template_name='termsofservice.html')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
