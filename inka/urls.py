from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('document/', views.document, name='document'),
    path('introduce/', views.introduce, name='introduce'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),  
    path('document/Django/django1', views.djangosetup, name='djangosetup'),  
    path('document/Django/django2', views.htmlwork, name='htmlwork'),      
]


