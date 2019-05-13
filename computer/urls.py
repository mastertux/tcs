from django.conf.urls import url
from django.urls import path
from computer import views

urlpatterns = [
  url(r'list/', views.ComputerList.as_view(), name='computer_list'),
  url(r'new/', views.ComputerCreate.as_view(), name='computer_new'),
  path(r'edit/<int:pk>/', views.ComputerUpdate.as_view(), name='computer_edit'),
  path(r'delete/<int:pk>/', views.ComputerDelete.as_view(), name='computer_delete'),

]