# myapp/serializers.py
from rest_framework import serializers
from .models import Student, StudentDetails

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# class StudentDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentDetails
#         fields = '__all__'


from .models import StudentDetails

class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'