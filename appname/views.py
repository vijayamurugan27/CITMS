from django.shortcuts import render

# Create your views here.
from appname.models import Student

def index1(request):
    name = 'Ravi'
    student  = Student.objects.get(id = 4)
    context = {'student':student  ,'name': name}
    return render (request, 'index10.html', context)


def index(request):
    return render(request, 'index.html')

def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Shop(request):
    return render(request, 'shop.html')

def Contact(request):
    return render(request, 'contact.html')

# Class based views

from django.shortcuts import render, redirect

from .models import StudentDetails

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class Forms(CreateView):
    model = StudentDetails
    fields = "__all__"
    template_name = 'CBV/forms.html'
    success_url = '/'

class StudentList(ListView):
    model = StudentDetails
    template_name = 'CBV/stulist.html'

class StudentDetail(DetailView):
    model = StudentDetails
    template_name = 'CBV/studetail.html'

class StudentUpdate(UpdateView):
    model = StudentDetails
    fields = '__all__'
    template_name = 'CBV/stuupdate.html'
    success_url = '/'

class StudentDelete(DeleteView):
    model = StudentDetails
    template_name = 'CBV/studelete.html'
    success_url = '/'

## for REST API 
from rest_framework import generics
from .models import Student, StudentDetails
from .serializers import StudentSerializer

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentDetailsListCreate(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentDetailsSerializer

# class StudentDetailsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentDetailsSerializer

# myapp/views.py
from rest_framework import generics
from .models import StudentDetails
from .serializers import StudentDetailsSerializer

class StudentDetailsListCreate(generics.ListCreateAPIView):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentDetailsSerializer

class StudentDetailsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentDetailsSerializer
