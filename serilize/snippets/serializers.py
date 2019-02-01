# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     seri
   Description :
   Author :       me
   date：          2019/1/28
-------------------------------------------------
   Change Activity:
                   2019/1/28:
-------------------------------------------------
"""
__author__ = 'me'
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


#
# class SnippetSerializer(serializers.ModelSerializer):
#     '''
#     重要的是要记住，ModelSerializer类并不会做任何特别神奇的事情，它们只是创建序列化器类的快捷方式：
#
#     一组自动确定的字段。
#     默认简单实现的create()和update()方法。
#     '''
#     #owner关联序列化器
#     class Meta:
#         model = Snippet
#         owner = serializers.ReadOnlyField ( source='owner.username' )
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
#
#
# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')