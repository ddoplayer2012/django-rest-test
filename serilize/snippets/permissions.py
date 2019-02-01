# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     permissions
   Description :
   Author :       me
   date：          2019/1/31
-------------------------------------------------
   Change Activity:
                   2019/1/31:
-------------------------------------------------
"""
__author__ = 'me'

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它。
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    """

    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求，
        # 所以我们总是允许GET，HEAD或OPTIONS请求。
        if request.method in permissions.SAFE_METHODS:
            return True

        # 只有该snippet的所有者才允许写权限。
        return obj.owner == request.user

