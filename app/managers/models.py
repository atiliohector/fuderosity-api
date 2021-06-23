from django.db import models

class ManagersModel(models.Model):
    
    name = models.CharField('Name', max_length=255, blank=False)
    age = models.PositiveIntegerField('Age', default=18, blank=False)
    champions = models.PositiveIntegerField('Champions', default=0, blank=False)
    champion_name = models.CharField('Champion Name', max_length=255, blank=False)

    def __str__(self):
        return self.name