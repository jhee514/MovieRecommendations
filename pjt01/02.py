import copy
import csv

import requests
from decouple import config

API_KEY = config('API_KEY')
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd='

result = {}
data_list = []

with open('boxoffice.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        data = requests.get(URL+item[0]).json()
        infos = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'audits', 'openDt', 'showTm', 'genres', 'directors', ]
        for info in infos:
            result[f'{info}'] = data['movieInfoResult']['movieInfo'][f'{info}']
        if data['movieInfoResult']['movieInfo']['audits']:
            result['audits'] = data['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm']
        if data['movieInfoResult']['movieInfo']['genres']:
            result['genres'] = data['movieInfoResult']['movieInfo']['genres'][0]['genreNm']
        if data['movieInfoResult']['movieInfo']['directors']:
            result['directors'] = data['movieInfoResult']['movieInfo']['directors'][0]['peopleNm']
        data_list.append(copy.copy(result))

with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'audits', 'openDt', 'showTm', 'genres', 'directors']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for info in data_list:
        writer.writerow(info)
