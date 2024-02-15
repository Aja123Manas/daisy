
from django.contrib import admin
from django.urls import path
from biashara import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.home),
    path('', views.images),
    path('about/', views.about),
    path('contact/', views.contact),
]
