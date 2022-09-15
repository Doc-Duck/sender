from django.db import models


class MassageList(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=150)
    filters = models.CharField(max_length=150)
    end_time = models.DateTimeField()


class Clients(models.Model):
    number = models.IntegerField(unique=True)
    code = models.IntegerField()
    tag = models.CharField(max_length=150)
    timezone = models.CharField(max_length=150)


class Messages(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=150)
    massage_list = models.ForeignKey('MassageList', on_delete=models.CASCADE)
    client = models.ForeignKey('Clients', on_delete=models.CASCADE)

