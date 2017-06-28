# -*- coding: utf-8 -*-

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Zixun, Picture, SS
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets', 'password')


class ZixunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zixun
        fields = ('id', 'title', 'category', 'source', 'update_time', 'see_times', 'publish_status')

class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'title', 'category', 'isComment', 'publish_time', 'content', 'picture_list')

class SSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SS
        fields = ('id', 'name', 'qq', 'wechat', 'alipay', 'buy_time', 'end_time', 'ss_ip', 'ss_port', 'ss_passwd', 'ss_encry', 'isExpired', 'note')
