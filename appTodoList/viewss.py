from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import generics, status
from appTodoList.models import Todolist
from appTodoList.serializers import TodolistSerializer


# Create your views here.

@csrf_exempt
def TodolistApi(self, request, *args, **kwargs):
    def get(self, request, *args, **kwargs):
        todolist=Todolist.objects.all()
        todolist_serializer=TodolistSerializer(todolist,many=True)
        return JsonResponse(todolist_serializer.data,safe=False)

    def post(self, request, *args, **kwargs):
        todolist_data=JSONParser().parse(request)
        todolist_serializer=TodolistSerializer(data=todolist_data)
        if todolist_serializer.is_valid():
            todolist_serializer.save()
            return JsonResponse("added Succesfully", safe=False)
        return JsonResponse("Failed to Add",safe=False)

    def put(self, request, *args, **kwargs):
        todolist_data=JSONParser().parse(request)
        todolist=Todolist.objects.get(Id=todolist_data['Id'])
        todolist_serializer=TodolistSerializer(todolist,data=todolist_data)
        if todolist_serializer.is_valid():
            todolist_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")

    def delete(self, request, *args, **kwargs):
        print( "+++++++++++++++++++++++++++++++++++++++")
        print( self.kwargs['id'])
        todolist=Todolist.objects.get(Id=id)
        todolist.delete()
        return JsonResponse("Deleted Successfully", safe=False)