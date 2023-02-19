from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor')
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(max_length=100, null=True)
