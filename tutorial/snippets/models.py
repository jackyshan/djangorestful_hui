# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets')
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
	    """
	    使用pygments来创建高亮的HTML代码。
	    """
	    lexer = get_lexer_by_name(self.language)
	    linenos = self.linenos and 'table' or False
	    options = self.title and {'title': self.title} or {}
	    formatter = HtmlFormatter(style=self.style, linenos=linenos,
	                              full=True, **options)
	    self.highlighted = highlight(self.code, lexer, formatter)
	    super(Snippet, self).save(*args, **kwargs)

class Zixun(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    category = models.TextField(default='')
    source = models.TextField(default='')
    update_time = models.TextField(default='')
    see_times = models.TextField(default='')
    publish_status = models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)

class Picture(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    category = models.TextField(default='')
    isComment = models.BooleanField(default=False)
    publish_time = models.TextField(default='')
    content = models.TextField(default='')
    picture_list = models.TextField(default='')

    class Meta:
        ordering = ('created',)
        
class SS(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    qq = models.TextField(default='')
    wechat = models.TextField(default='')
    alipay = models.TextField(default='')
    buy_time = models.TextField(default='')
    end_time = models.TextField(default='')
    ss_ip = models.TextField(default='')
    ss_port = models.TextField(default='')
    ss_passwd = models.TextField(default='')
    ss_encry = models.TextField(default='aes-256-cfb')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(default='')

    class Meta:
        ordering = ('created',)
        