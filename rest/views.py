from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from django.core import serializers
from .serializers import employeesSerializer

class employeeList(APIView):

    def get(self,request):
        employee1 = employees.objects.all()
        serializer = employeesSerializer(employee1, many=True)  #converting employees model data to JSON objects
        return Response(serializer.data)  #to convert to JSON

    def post(self):
        pass
