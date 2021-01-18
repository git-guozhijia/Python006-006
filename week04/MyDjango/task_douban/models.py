from django.db import models



class Comments(models.Model):
    comments = models.CharField(max_length=400, null=True)
    star_review = models.FloatField(null=True)
    comments_time = models.DateTimeField(null=True)

    class Meta:
        managed = False
        db_table = 'comments'