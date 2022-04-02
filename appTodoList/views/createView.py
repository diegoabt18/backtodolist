from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import generics, status
from appTodoList.models import Todolist
from appTodoList.serializers import TodolistSerializer
import json


class CreateView(generics.CreateAPIView):
  
    def post(self, request, *args, **kwargs):
        todolist_data=JSONParser().parse(request)
        todolist_serializer=TodolistSerializer(data=todolist_data)
        if todolist_serializer.is_valid():
            todolist_serializer.save()
            return JsonResponse("added Succesfully", safe=False)
        return JsonResponse("Failed to Add",safe=False)

