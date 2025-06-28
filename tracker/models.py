from django.db import models

class Entry(models.Model):
    TYPE_CHOICES = [('Intake', 'Intake'), ('Burn', 'Burn')]

    date = models.DateField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.date} - {self.type} - {self.calories} kcal"
