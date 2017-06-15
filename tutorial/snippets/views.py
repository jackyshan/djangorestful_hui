# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#------------------------下面是django模板---------------------------
from django.shortcuts import render
from snippets.models import Zixun, Picture
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import os,time

@login_required(login_url='/login')
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
    queryset = Picture.objects.all()
    return render(request, 'picture-list.html', {'pictures': queryset})
def picture_add(request):
    return render(request, 'picture-add.html')
def picture_show(request):
    return render(request, 'picture-show.html')

def login_index(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    print request.POST
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'index.html')
        else:
            print 'disabled account'
            return render(request, 'login.html', {'errmsg': 'disabled account'})
            # Return a 'disabled account' error message
    else:
        print 'invalid login'
        return render(request, 'login.html', {'errmsg': 'invalid login'})
        # Return an 'invalid login' error message.

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    print '退出登录'
    return render(request, 'login.html')

def handle_uploaded_file(f):
    path = 'static/upload/'+time.strftime("%Y%m%d%H%m%s", time.localtime())+f.name
    # path = os.path.join('static/upload/name.png')
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        return path

def upload_file(request):
    if request.method == 'POST':
        print request.FILES
        url = handle_uploaded_file(request.FILES['file'])
        print url
        return HttpResponse(url)
    return HttpResponse('ok')

#用户注册
def register(request):
    if request.method == 'GET':
        return HttpResponse('ok')
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username=username, email=password, password=password)
    user.save()
    return HttpResponse('register succ')

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
from rest_framework import mixins

# class UserViewSet(mixins.CreateModelMixin,
#                                 mixins.ListModelMixin,
#                                 mixins.RetrieveModelMixin,
#                                 viewsets.GenericViewSet):
#     """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.

#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


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
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)
    permission_classes = (permissions.IsAuthenticated,)

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

#---------------------------picture
from snippets.serializers import PictureSerializer
from snippets.models import Picture
class PictureViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer