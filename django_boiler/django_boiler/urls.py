"""django_boiler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include

from core.views import index

from . import routes

from api.urls import router as api
from api.views import book

router = routes.DefaultRouter()

router.extend(api)

urlpatterns = [
    path('admin/', admin.site.urls),    
    re_path(r'^(api(/)?)', include(router.urls)),
    re_path(r'^(?!api/)(?P<path>)', index, name='index')
]
 
# ^ beginning of line
# (?!api) not followed by 'api'
# .* followed by 0 or more characters
# re_path(r'^(?!api(/)?)(?P<path>)', index, name='index'), # works