import codecs
from scraping_app.parsers import *


parsers = ((get_work_data, 'https://www.work.ua/ru/jobs-python/'),
           (get_rabota_data, 'https://www.rabota.ru/vacancy/?query=python&sort=relevance')
           )

jobs, errors = [], []
for func, url in parsers:
    job, error = func(url)
    jobs += job
    errors += error

result = codecs.open('work.json', 'w', 'utf-8')
result.write(str(jobs))
result.close()