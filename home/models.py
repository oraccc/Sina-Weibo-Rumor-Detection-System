from django.db import models


from datetime import datetime


class unverified_weibo(models.Model):
	username = models.CharField(max_length=200)
	content = models.CharField(max_length=500)
	public_time = models.DateTimeField(default=datetime.now)
	img_url = models.CharField(max_length=200)
	dianzan = models.IntegerField()
	zhuanfa = models.IntegerField()
	pinglun = models.IntegerField()
	fake_type = models.CharField(max_length=200)

class verified_weibo(models.Model):
	username = models.CharField(max_length=200)
	content = models.CharField(max_length=500)
	public_time = models.DateTimeField(default=datetime.now)
	img_url = models.CharField(max_length=200)
	dianzan = models.IntegerField()
	zhuanfa = models.IntegerField()
	pinglun = models.IntegerField()
	fake_type = models.CharField(max_length=200)
