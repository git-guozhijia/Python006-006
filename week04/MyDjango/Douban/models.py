from django.db import models

class T1(models.Model):
    n_star = models.IntegerField()
    short = models.CharField(max_length=400)
    sentiment = models.FloatField()

    class Meta:
        managed = False
        db_table = 't1'