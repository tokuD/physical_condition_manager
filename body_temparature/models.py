from django.db import models
from django.conf import settings

class Log(models.Model):
    """体温記録"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='名前')
    body_temp = models.FloatField('体温')
    day = models.DateField('日付', auto_now_add=True)

    def __str__(self):
        return str(self.user) + ':' + str(self.day)