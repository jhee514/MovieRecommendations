import urllib

import requests
from decouple import config


def send_naver_movie(movie_name):
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')
    BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
    URL = BASE_URL + '?query=' + movie_name
    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret,
    }
    response = requests.get(URL, headers=headers)
    return response.json()

def send_naver_movie_img(movie_name):
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')
    BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
    URL = BASE_URL + '?query=' + movie_name
    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret,
    }
    response = requests.get(URL, headers=headers) 
    return response.json()['items'][0]['image']
