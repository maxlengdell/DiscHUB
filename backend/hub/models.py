from django.db import models

# Create your models here.
class Disc(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    speed = models.IntegerField()

    def _str_(self):
        return self.title