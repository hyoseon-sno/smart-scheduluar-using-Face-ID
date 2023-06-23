from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),

    path('main/', views.main),
    path('user/', views.user),
    path('index/',views.index),      
    path('calendar/',views.CalendarView.as_view()),
]
