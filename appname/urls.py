"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from appname import views

from .views import Forms, StudentList, StudentDetail, StudentUpdate, StudentDelete
from .views import StudentListCreate, StudentRetrieveUpdateDestroy
from .views import StudentDetailsListCreate, StudentDetailsRetrieveUpdateDestroy

urlpatterns = [
path('index1', views.index1, name = 'index1'),

path('index', views.index, name = 'index'),
path('home', views.Home, name = 'home'),
path('about', views.About, name = 'about'),
path('shop', views.Shop, name = 'shop'),
path('contact', views.Contact, name = 'contact'),

path('forms', Forms.as_view(), name = 'forms'),
path('', StudentList.as_view(), name = 'list'),
path('<pk>/detail', StudentDetail.as_view(), name = 'detail'),
path('<pk>/update', StudentUpdate.as_view(), name = 'update'),
path('<pk>/delete', StudentDelete.as_view(), name = 'delete'),

## for API VIEW

path('students/', StudentListCreate.as_view(), name='student-list-create'),
path('students/<int:pk>/', StudentRetrieveUpdateDestroy.as_view(), name='student-detail'),



# path('studentsDetails/', StudentDetailsListCreate.as_view(), name='student-list-create'),
# path('studentsDetails/<int:pk>/', StudentDetailsRetrieveUpdateDestroy.as_view(), name='student-detail'),

path('studentdetails/', StudentDetailsListCreate.as_view(), name='studentdetails-list-create'),
path('studentdetails/<int:pk>/', StudentDetailsRetrieveUpdateDestroy.as_view(), name='studentdetails-detail'),



]
