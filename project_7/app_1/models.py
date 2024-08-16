from django.db import models


class ComputerisationTechnical(models.Model):
    link = models.TextField('Ссылка')
    price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField('Описание')

    def __str__(self):
        return f'{self.price} | {self.description[:60]}'
