#from msilib.schema import Class
from rest_framework import serializers
from appTodoList.models import Todolist

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todolist
        fields=('tl_id','tl_title','tl_description', 'tl_date', 'tl_task', 'tl_state' )
