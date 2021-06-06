from django.db import models

class EmployeesModels(models.Model):
    
    class Meta:
       db_table = 'employees'

    name = models.CharField('Name', max_length=255, blank=False)
    age = models.PositiveBigIntegerField('Age', blank=False, default=18)
    position = models.CharField('Position', max_length=255, blank=False)
    
    def __str__(self):
        return self.name