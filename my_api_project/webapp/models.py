from django.db import models


class Person (models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    user_id = models.IntegerField()

    def __str__(self):
        return self.firstName

