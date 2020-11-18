from django.db import models


SEX_CHOICES = (
    ('female', 'female'),
    ('male', 'male')
)

class SuicideStat(models.Model):
    country = models.CharField(max_length=200, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    age = models.CharField(max_length=20, null=True, blank=True)
    suicides_no = models.CharField(max_length=20, null=True, blank=True)
    population = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('country',)

    def __str__(self):
        return self.country

    
    
