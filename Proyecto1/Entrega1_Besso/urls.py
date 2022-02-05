"""Entrega1_Besso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Entrega1_Besso.views import saludo, otro_saludo, template1, template2, template3, template4




urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludo/", saludo),
    path("segundosaludo/", otro_saludo),
    path("template1/", template1),
    path("template2/", template2),
    path("template3/<nombre>", template3),
    path("template4/", template4),
]
