# Counter_assig/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('incrementby2', views.increment_by_2_view, name='increment_by_2'),
    path('increment', views.increment_view, name='increment'),
    path('destroy_session', views.destroy_session_view, name='destroy_session'),
    path('reset', views.reset_counter_view, name='reset_counter'),
]
