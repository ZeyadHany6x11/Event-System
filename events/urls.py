from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('event/<int:id>/', views.event_details, name='details'),

    path('book/<int:id>/', views.book_event, name='book'),

]