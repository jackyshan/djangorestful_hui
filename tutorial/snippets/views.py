# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#------------------------下面是django模板---------------------------
from django.shortcuts import render
from snippets.models import Zixun
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')
def welcome(request):
    print '/welcome调用'
    return render(request, 'welcome.html')
def artical_list(request):
    queryset = Zixun.objects.all()
    return render(request, 'article-list.html', {'zixuns': queryset})
def article_add(request):
    if request.method == 'POST':
        print 'post----->>>'
        print request.POST['articletitle']
        return HttpResponse('ok')
    return render(request, 'article-add.html')
def picture_list(request):
    return render(request, 'picture-list.html')
def picture_add(request):
    return render(request, 'picture-add.html')
    
#---------------------------下面是接口---------------------------
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer
#---------------------------user
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


#---------------------------snippet
from rest_framework.decorators import detail_route

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#---------------------------zixun
from snippets.serializers import ZixunSerializer
from snippets.models import Zixun
class ZixunViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Zixun.objects.all()
    serializer_class = ZixunSerializer