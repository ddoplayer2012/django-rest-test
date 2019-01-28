# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers.py
   Description :
   Author :       me
   date：          2019/1/25
-------------------------------------------------
   Change Activity:
                   2019/1/25:
-------------------------------------------------
"""
__author__ = 'me'
# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed', 'create_date')