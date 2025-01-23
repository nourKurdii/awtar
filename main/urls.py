from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('tenders/', views.tender, name='tender'),
    path('activities/', views.activities, name='activities'),
    path('activity/', views.activity, name='activity'),
    path('events/', views.events, name='events'),
    path('event/', views.event, name='event'),
    path('activity_form/', views.activity_form, name='activity_form'),
    path('blog/', views.blog, name='blog'),
]