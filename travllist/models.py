# coding=utf-8
from django.db import models


class User(models.Model):
    username = models.CharField(u'用户名', max_length=30, unique=True)
    password = models.CharField(u'密码', max_length=30)
    create_time = models.DateTimeField(u'注册时间', auto_now_add=True)
    last_modify_time = models.DateTimeField(u'最后修改时间', auto_now=True)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u'注册用户'
        verbose_name_plural = u'注册用户'


class Travel(models.Model):
    travel_code = models.CharField(u'旅游代码', max_length=30)
    travel_date = models.CharField(u'旅游日期', max_length=20)
    adult_price = models.CharField(u'成人价', max_length=30, null=True, blank=True)
    child_price = models.CharField(u'儿童价', max_length=30, null=True, blank=True)
    get_time = models.CharField(u'采集时间', max_length=30, null=True, blank=True)
    remark = models.CharField(u'备注', max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.travel_code

    class Meta:
        verbose_name = u'旅游信息'
        verbose_name_plural = u'旅游信息'
