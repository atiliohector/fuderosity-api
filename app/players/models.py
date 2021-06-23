from django.db import models

class PlayersModels(models.Model):

    name = models.CharField('Name', max_length=255, blank=False)
    age = models.PositiveIntegerField('Age', default=18, blank=False)
    position = models.CharField('Position', max_length=255, blank=False)
    guild = models.CharField('Guild', max_length=255, default='Alone')

    def __str__(self):
        return self.name