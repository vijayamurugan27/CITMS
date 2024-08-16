from django.urls import path
from api import views

from .views import getData, addItem, updateItem, deleteItem


urlpatterns = [
    path('', views.getData, name = 'student-list'), 
    path('add/', views.addItem, name = 'student-add'),
    path('update/<int:pk>/', updateItem, name='student-update'),
    path('delete/<int:pk>/', deleteItem, name='student-delete'),
]
