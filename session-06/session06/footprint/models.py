from django.db import models


class Footprint(models.Model):
    footprint_id = models.AutoField(primary_key=True)
    receiver = models.TextField(null=False)
    message = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True, blank=True)
