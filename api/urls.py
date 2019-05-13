from django.conf.urls import url
from api import views

urlpatterns = [
  url(r'computers/', views.computer_list, name='api_computer_list'),
  url(r'computers_status/', views.computer_status_list, name='api_computers_status_list'),
  url(r'computer_events/', views.save_randon_events, name='api_save_computer_events')
]