from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=250, verbose_name='Датчик')
    description = models.TextField(max_length=250, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['name']

    def __str__(self):
        return self.name


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата внесения')

    class Meta:
        verbose_name = 'Показание'
        verbose_name_plural = 'Показания'
        ordering = ['created_at']

    def __str__(self):
        return f' {str(self.temperature)}C" at {str(self.created_at)[:16]}'

