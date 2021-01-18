from django.db import models

# Create your models here.

class Type(models.Model):
	# id = models.AutoField(primary_key=True) # django会自动创建id字段并设置为自增和主键
	typename = models.CharField(max_length=20)

class Name(models.Model):
	name = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	stars = models.CharField(max_length=10)
	# extend = models.CharField(max_length=150)

