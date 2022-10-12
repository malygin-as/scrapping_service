import requests
import codecs
from bs4 import BeautifulSoup as bs
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

__all__ = ('get_work_data', 'get_rabota_data')

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

user_agents = user_agent_rotator.get_user_agents()

user_agent = user_agent_rotator.get_random_user_agent()

headers = {'UserAgent': user_agent,
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           }

def get_work_data(url):
    domain = 'https://www.work.ua'
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

    return jobs, errors


def get_rabota_data(url):
    domain = 'https://www.rabota.ru'
    resp = requests.get(url, headers=headers)
    jobs = []
    errors = []

    if resp.status_code == 200:
        soup = bs(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'class': 'infinity-scroll r-serp__infinity-list'})
        if main_div:
            div_list = main_div.findAll('div', attrs={'class': 'vacancy-preview-card__top'})
            for div in div_list:
                title = div.find('h3')
                href = title.a['href']
                description = div.find('div', attrs={'class': 'vacancy-preview-card__short-description'})
                company = div.find('span', attrs={'class': 'vacancy-preview-card__company-name'}).a
                jobs.append({'title': title.text,
                             'url': domain + href,
                             'description': description.text,
                             'company': company.text})
        else:
            errors.append({'url': url, 'title': 'Main div does not exist'})
    else:
        errors.append({'url': url, 'title': f'Site does not response {resp.status_code}'})

    return jobs, errors
