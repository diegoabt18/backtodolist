from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import generics, status
from appTodoList.models import Todolist
from appTodoList.serializers import TodolistSerializer
import json

class UpdateView(generics.UpdateAPIView):
     def put(self, request, *args, **kwargs):
        todolist_data=JSONParser().parse(request)
        todolist=Todolist.objects.get(tl_id=todolist_data['id'])
        todolist_serializer=TodolistSerializer(todolist,data=todolist_data)
        if todolist_serializer.is_valid():
            todolist_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")


