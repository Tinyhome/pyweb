#coding:utf-8


from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.
class myuser(models.Model):
    id = models.AutoField
    user_name = models.CharField(max_length=30)
    user_pass = models.CharField(max_length=50)
    user_regdate=models.DateTimeField(default=datetime.datetime.now())
    user_status=models.IntegerField(default=1)   #1代表有效用户 2代表vip用户
    

    class Meta:
        
        db_table = 'myuser'
