import copy
import csv
import time
import urllib.parse as urlparse

import requests

from naver_API import send_naver_movie, send_naver_movie_img


movie_names = []
info_list = []
result = {}

with open('./boxoffice.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    for line in reader:
        movie_names.append(line[1])

for movie_name in movie_names:
    time.sleep(0.5)
    u = send_naver_movie(movie_name)['items'][0]['link']
    result['movieCd'] = urlparse.parse_qs(urlparse.urlparse(u).query)['code'][0]
    result['title'] = movie_name
    infos = ['link', 'image', 'userRating']
    for info in infos:
        if send_naver_movie(movie_name)['items'][0][f'{info}']:
            result[f'{info}'] = send_naver_movie(movie_name)['items'][0][f'{info}']
    info_list.append(copy.copy(result))

with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'title', 'link', 'image', 'userRating']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for result_info in info_list:
        writer.writerow(result_info)
