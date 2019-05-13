from django.conf.urls import url
from django.urls import path
from computer_status import views

urlpatterns = [
  url(r'list/', views.ComputerStatusList.as_view(), name='computer_status_list'),
  url(r'new/', views.ComputerStatusCreate.as_view(), name='computer_status_new'),
  path(r'edit/<int:pk>/', views.ComputerStatusUpdate.as_view(), name='computer_status_edit'),
  path(r'delete/<int:pk>/', views.ComputerStatusDelete.as_view(), name='computer_status_delete'),

]