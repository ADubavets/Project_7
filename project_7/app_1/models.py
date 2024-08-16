from django.db import models


class Car(models.Model):
    name = models.CharField('Наименование автомобиля', max_length=30)
