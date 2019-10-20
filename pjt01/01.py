import copy
import csv
from datetime import datetime, timedelta

import requests
from decouple import config

API_KEY = config('API_KEY')
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={API_KEY}&weekGb=0&targetDt='

top_10 = []
result = {}
cd_list = []

for n in range(50):
    dt = datetime(2019, 7, 13) - timedelta(weeks=n)
    data = requests.get(URL+dt.strftime("%Y%m%d")).json()
    for movie in data['boxOfficeResult']['weeklyBoxOfficeList']:
        if not movie['movieCd'] in cd_list:
            items = ['movieNm', 'movieCd', 'audiAcc']
            for item in items:
                result[f'{item}'] = movie[f'{item}']
            top_10.append(copy.copy(result))
            cd_list.append(copy.copy(movie.get('movieCd')))

with open ('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'movieNm', 'audiAcc']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for movie in top_10:
        if movie:
            writer.writerow(movie)
