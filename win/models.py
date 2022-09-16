from django.db import models

class Participants (models.Model):
    name=models.CharField(max_length=40)
    document=models.IntegerField(max_length=8)
    age=models.IntegerField()
    country=models.CharField(max_length=50)
    description=models.CharField(max_length=400)

    def __str__(self):
        return self.name