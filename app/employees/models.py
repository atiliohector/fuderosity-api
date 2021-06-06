from django.db import models

class EmployeeModel(models.Model):

    class Meta:
        db_table = 'employees'

    name = models.CharField('name', max_length=255, blank=False)
    age = models.PositiveIntegerField('age', default=18, blank=False)
    position = models.CharField('position', blank=False, max_length=30)

    def __str__(self):
        return self.name