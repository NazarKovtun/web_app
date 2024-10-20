from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('come_on', views.come_on, name='come_on'),
    path('contacts', views.contacts, name='contacts')
]
