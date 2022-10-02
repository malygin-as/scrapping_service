from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name='Наименование города',
                            unique=True)
    slug = models.CharField(max_length=30, blank=True,
                            unique=True)

    class Meta:
        verbose_name = 'Наименование города'
        verbose_name_plural = 'Наименования городов'

    def __str__(self):
        return self.name


class CodeLang(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name='Язык программирования',
                            unique=True)
    slug = models.CharField(max_length=30, blank=True,
                            unique=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name
