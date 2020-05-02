"""RNAseqDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include 
from django.contrib import admin 
from rest_framework import routers 
from RNAseqAPI.views import exp1Viewset, exp2Viewset 
router = routers.DefaultRouter() 
router.register('exp1',exp1Viewset) 
router.register('exp2',exp2Viewset)
# prefix = movies , viewset = MovieViewSet 

urlpatterns = [ 
    url(r'^admin/', admin.site.urls), 
    url(r'^',include(router.urls)), 
    ]

