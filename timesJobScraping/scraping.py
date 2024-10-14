from bs4 import BeautifulSoup
import requests
from datetime import date
import time

def main():
    html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_file, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    skill_black_list = ['machine learning', 'kubernetes', 'gateway']
    post = ''

    for job in jobs:

        posted_at = job.find('span', class_='sim-posted').span.text
        if posted_at != 'Posted few days ago':
            continue

        link = job.header.h2.a['href']
        company_name = job.find('h3', class_='joblist-comp-name').text.strip().replace('\n', ' ')
        skills: str = job.find('span', class_='srp-skills').text.strip().replace('\n', ', ').replace('  ', ', ')

        skip = False
        for skill in skill_black_list:
            if skill in skills:
                skip = True
        if skip:
            continue

        post += f'Company name: {company_name} \nSkills required: {skills} \nMore info: {link} \n\n'

    with open(f'./timesJobScraping/posts/{date.today()}.txt', 'w') as p:
        p.write(post)

    
if __name__ == '__main__':
    while True:
        main()
        print('Waiting...')
        time.sleep(3600 * 24)