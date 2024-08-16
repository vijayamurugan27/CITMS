from django.forms import ModelForm

from appname.models import Student

class ContactForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'