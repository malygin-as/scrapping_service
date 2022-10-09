from django.db import models
from scraping_app.utils import from_cyrillic_to_eng


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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    company = models.CharField(max_length=50, verbose_name='Компания')
    description = models.TextField(verbose_name="Описание")
    salary = models.DecimalField(decimal_places=0, max_digits=8)
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    codelang = models.ForeignKey('CodeLang', on_delete=models.CASCADE, verbose_name='Язык программирования')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title
