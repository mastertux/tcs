from django.conf.urls import url
from django.urls import path
from events_generator import views

urlpatterns = [
  url(r'new/', views.RandomEventsFrequenceCreate.as_view(), name='randon_events_new'),
  path(r'edit/<int:pk>/', views.RandomEventsFrequenceUpdate.as_view(), name='randon_events_edit'),
]