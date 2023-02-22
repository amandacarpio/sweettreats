from django.db import models

# Create your models here.
class Selections(models.Model):
    Dessert_Name = models.CharField(max_length=50, blank=False)
    Allergies = models.BooleanField()
    If_yes_please_specify = models.CharField(max_length=100, null=True, blank=True)
    Dessert_Details = models.CharField(max_length=500, blank=False)
    Email = models.CharField(max_length=50, blank=False)
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'
    BUDGET_OPTIONS = [
        (Low, '$1-$50'),
        (Medium, '$51-$100'),
        (High, '$101 +'),
    ]
    Budget = models.CharField(
        max_length=6,
        choices=BUDGET_OPTIONS,
        default=Low,
    )
    