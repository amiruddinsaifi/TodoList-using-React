from rest_framework import  serializers
from .models import  employees,students
 

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        #fields={'firstName','lastName'}
        fields= '__all__'

class studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        #fields={'firstName','lastName'}
        fields= '__all__'