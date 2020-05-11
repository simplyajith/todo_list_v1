from django.shortcuts import render
from todo_app.models import Todo, TodoStatus
from .serializers import TodoSerializer,TodoStatusSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
import json
from django.http import Http404


class TodoViewSet(ModelViewSet):

   queryset = Todo.objects.all()
   serializer_class = TodoSerializer
   # lookup_field = 'task_uuid'

   def change_request_data(self,request):

      validated_data_status = request.data["status"].capitalize()
      if validated_data_status not in ["New", "In progress", "Completed"]:
         return False
      request.data["status"] = None
      if validated_data_status:
         status_obj = TodoStatus.objects.filter(status = validated_data_status)
         print(status_obj)
         status_s = TodoStatusSerializer(status_obj,many = True)
         print(status_s.data)
         if status_s.data:
            request.data["status"] = status_s.data[0].get("id",None)
      return request

   
   def create(self,request,pk=None):

      req = self.change_request_data(request)
      serializer = TodoSerializer(data= req.data)
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def get_todo(self, pk):

         todo_ins = get_object_or_404(Todo, pk=pk)
         return todo_ins
   
   def update(self, request,pk):
      
      todo_ins = self.get_todo(pk)
      req = self.change_request_data(request)
      if not req:
         invalid_data = {"error":"Not valid status data"}
         return Response(invalid_data, status=status.HTTP_400_BAD_REQUEST )
      serializer = TodoSerializer(todo_ins, data = req.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
         
class TodoStatusViewSet(ModelViewSet):

   queryset = TodoStatus.objects.all()
   serializer_class = TodoStatusSerializer

