import requests
import codecs
from bs4 import BeautifulSoup as bs

headers = {'UserAgent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           }

domain = 'https://www.work.ua'
url = 'https://www.work.ua/ru/jobs-python/'
resp = requests.get(url, headers=headers)
jobs =[]
errors = []

if resp.status_code == 200:
    soup = bs(resp.content, 'html.parser')
    main_div = soup.find('div', id='pjax-job-list')
    if main_div:
        div_list = main_div.findAll('div', attrs={'class': 'job-link'})
        for div in div_list:
            title = div.find('h2')
            href = title.a['href']
            description = div.p.text
            company = div.find('div', attrs={'class': 'add-top-xs'}).span.b.text
            jobs.append({'title': title.text.replace('\n',''),
                         'url': domain + href,
                         'description': description.replace('\n',''),
                         'company': company})
    else:
        errors.append({'url': url, 'title': 'Main div does not exist'})
else:
    errors.append({'url': url, 'title': f'Site does not response {resp.status_code}'})

h = codecs.open('work.json', 'w', 'utf-8')
h.write(str(jobs))
h.close()
