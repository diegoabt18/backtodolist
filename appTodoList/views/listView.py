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
        todolist_serializer=TodolistSerializer(todolist,many=True)
        if todolist_serializer.is_valid():
            return JsonResponse(todolist_serializer.data,safe=False)
        return JsonResponse("Failed to Add",safe=False)
