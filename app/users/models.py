from django.db import models

class UserModel(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(default=18, blank=True, null=True)


    def __str__(self):
        return self.name