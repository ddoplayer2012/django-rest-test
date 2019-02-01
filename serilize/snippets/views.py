from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import renderers
from rest_framework.response import Response

class SnippetHighlight(generics.GenericAPIView):
    '''
    高亮渲染器
    '''
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
#
# class snippet_list(APIView):
#     """
#     列出所有的snippets，或者创建一个新的snippet。
#     """
#     def get(self,request,format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets,many=True)
#         return Response(serializer.data)
#
#     def post(self,request,format=None):
#         serializer = SnippetSerializer(request.data,many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return  Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#
# class snippet_detail(APIView):
#     """
#     列出所有的snippets，或者创建一个新的snippet。
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return  Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class SnippetList(generics.ListCreateAPIView):
    '''
    进一步简化ListCreateAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView)
    GET ,POST
    '''
    #queryset为必须字段，assert里面有断言，如果为None则报错
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #修改这里就能控制该视图路由的权限

    def perform_create(self, serializer):
        serializer.save ( owner=self.request.user )


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    进一步简化generics.RetrieveUpdateDestroyAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView)
    GET,POST,PATCH,DELETE
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,) #修改这里就能控制该视图路由的权限

#
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     '''
#     retrieve() 检索模块实例         返回：return Response(serializer.data)
#     '''
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer