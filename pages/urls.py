from django import views
from django.urls import path
from . import views
urlpatterns=[
    path('',views.HomePageView.as_view(),name='home')
    
]