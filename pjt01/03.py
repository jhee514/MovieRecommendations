import copy
import csv

import requests
from decouple import config

API_KEY = config('API_KEY')
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={API_KEY}&peopleNm='

result = {}
data_list = []
directors =[]

with open('movie.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        data = requests.get(URL+str(item[-1])).json()
        if data['peopleListResult']['peopleList']:
            if not data['peopleListResult']['peopleList'][0]['peopleNm'] in directors:
                profiles = ['peopleCd', 'peopleNm', 'repRoleNm', 'filmoNames',]
                for profile in profiles:
                    result[f'{profile}'] = data['peopleListResult']['peopleList'][0][f'{profile}']
                data_list.append(copy.copy(result))
                directors.append(copy.copy(result['peopleNm']))

with open ('director.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['peopleCd', 'peopleNm', 'repRoleNm', 'filmoNames']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for profile in data_list:
        writer.writerow(profile)
