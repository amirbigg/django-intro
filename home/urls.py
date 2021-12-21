from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('details/<int:todo_id>/', views.detail, name='details'),
	path('delete/<int:todo_id>/', views.delete, name='delete'),
]