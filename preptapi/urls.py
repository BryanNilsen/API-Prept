"""preptapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
# TODO: explicitly list out models and views >> Pythonic
from preptrestapi.models import *
from preptrestapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'profiles', ProfileViewSet, 'profiles')
router.register(r'foods', FoodViewSet, 'foods')
router.register(r'waters', WaterViewSet, 'waters')
router.register(r'members', MemberViewSet, 'members')
router.register(r'users', UserViewSet, 'users')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]