from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import generics, status
from appTodoList.models import Todolist
from appTodoList.serializers import TodolistSerializer

class ListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        todolist=Todolist.objects.all()
        print("aqui esta el todolist")
        print(todolist)
        print("aqui esta el serializer")
        todolist_serializer=TodolistSerializer(todolist,many=True)
        print(todolist_serializer)
        return JsonResponse(todolist_serializer.data,safe=False)
