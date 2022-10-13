import codecs
import os
import sys


project = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project)
os.environ['DJANGO_SETTINGS_MODULE'] = 'scrapping_service.settings'

import django
django.setup()
from django.db import DatabaseError

from scraping_app.parsers import *
from scraping_app.models import Vacancy, City, CodeLang, Error

parsers = ((get_work_data, 'https://www.work.ua/ru/jobs-python/'),
           (get_rabota_data, 'https://www.rabota.ru/vacancy/?query=python&sort=relevance')
           )

city = City.objects.filter(slug='moskva').first()
codelang = CodeLang.objects.filter(slug='python').first()

jobs, errors = [], []
for func, url in parsers:
    job, error = func(url)
    jobs += job
    errors += error

for job in jobs:
    vacancy = Vacancy(**job, city=city, codelang=codelang, salary=100)
    try:
        vacancy.save()
    except DatabaseError:
        pass
if errors:
    error = Error(data=errors).save()

with codecs.open('work.json', 'w', encoding='utf-8') as file:
    file.write(str(jobs))

with codecs.open('errors.json', 'w', encoding='utf-8') as file:
    file.write(str(errors))
