from django.db import models


class Newstats(models.Model):
    iphone = models.IntegerField()
    android = models.IntegerField()
    win = models.IntegerField()
    mac = models.IntegerField()
    others = models.IntegerField()