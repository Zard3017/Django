from django.contrib import admin
from django.urls import path
from ZardDjango import views
urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.index),
    path('welcome/', views.welcome),
    path('shule/', views.emobilis),
    path('home/', views.Home),
    path('services/', views.Services),
    path('contact/',views.Contact),
    path('about/',views.About, name='my-about')

]