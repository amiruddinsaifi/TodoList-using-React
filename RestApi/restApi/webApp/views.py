from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .models import students
from .serializers import employeesSerializer
from .serializers import studentsSerializer
# Create your views here.

class employeeList(APIView):
    def get(self,request):
        employees1=employees.objects.all();
        serializer=employeesSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class studentsList(APIView):
    def get(self,request):
        students1=students.objects.all();
        serializer=studentsSerializer(students1, many=True)
        return Response(serializer.data)

    def post(self):
        pass