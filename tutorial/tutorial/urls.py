"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'zixuns', views.ZixunViewSet)
router.register(r'pictures', views.PictureViewSet)
router.register(r'sss', views.SSViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^ss_list$', views.ss),
    url(r'^ss_add$', views.ss_add, name='ss_add'),
    url(r'^ss_edit/', views.ss_edit, name='ss_edit'),
    url(r'^register$', views.register),
    url(r'^upload_file$', views.upload_file),
    url(r'^login_out$', views.logout_view),
    url(r'^login$', views.login_index),
    url(r'^index$', views.index),
    url(r'^picture_add$', views.picture_add, name='picture_add'),
    url(r'^picture_show$', views.picture_show, name='picture_show'),
    url(r'^picture_list$', views.picture_list, name='picture_list'),
    url(r'^artical_list$', views.artical_list, name='artical_list'),
    url(r'^article_add$', views.article_add, name='article_add'),
    url(r'^welcome$', views.welcome, name='welcome'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^admin/', include(admin.site.urls)),
]
