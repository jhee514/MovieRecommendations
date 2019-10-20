import copy
import csv
import time

import requests

from naver_API import send_naver_movie, send_naver_movie_img

url_list = []

with open('movie_naver.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    for line in reader:
        result = {line[0]: line[3]}
        url_list.append(copy.copy(result))

for url in url_list:
    time.sleep(0.5)
    for movie_code, image_url in url.items():
        with open(f'./images/{movie_code}.jpg', 'wb') as f:
            image = requests.get(f'{image_url}', stream=True).content
            if image:
                f.write(image)
