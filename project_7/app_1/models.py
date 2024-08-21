from django.db import models


class ComputerisationTechnical(models.Model):
    link = models.TextField('Ссылка')
    price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField('Описание')
    parse_datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def get_absolute_url(self):
        return self.link

    def __str__(self):
        return f'{self.price} | {self.description[:60]}'

    class Meta:
        verbose_name = 'Компьютерная техника'
        verbose_name_plural = 'Компьютерная техника'
        ordering = ['-price', 'parse_datetime']
