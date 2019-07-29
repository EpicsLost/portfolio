from django.db import models

# 实现组件的功能
# Create your models here.
class Gallery(models.Model):
    description = models.CharField(max_length=100)