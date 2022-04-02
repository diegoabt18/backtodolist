from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import generics, status
from appTodoList.models import Todolist
from appTodoList.serializers import TodolistSerializer
import json


class DeteleView(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        todolist=Todolist.objects.get(Id=self.kwargs['id'])
        todolist.delete()
        return JsonResponse("Deleted Successfully", safe=False)

