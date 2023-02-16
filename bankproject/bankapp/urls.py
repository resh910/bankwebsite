from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('register/', views.register, name='register'),
    path('form/',views.form,name='form'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('usr/',views.usr,name='usr'),
    path('msg/',views.msg,name='msg'),
]