# Create your models here.
from django.db import models


# making a most of what the expected post call will be like
class Post(models.Model):
    # the inputs are all Floats
    lat = models.FloatField()
    lon = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    epoch = models.FloatField()
    orientation = models.FloatField()

    def __float__(self):
        return self.lat
