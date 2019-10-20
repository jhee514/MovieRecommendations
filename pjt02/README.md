---

typora-copy-images-to: ./movie_naver.csv_img.png
---

# Project 02

  Project 02에서는 앞서 Project 01에서 수집한 영화 데이터를 바탕으로 해당 영화들의 

## naver_API.py

- naver API를 활용하여 원하는 영화 정보 수집을 위한 함수를 작성하였다.

```python
import urllib

import requests
from decouple import config
```

  네이버 오픈 API 가운데 검색 API를 이용하여 원하는 영화에 대한 정보를 수집 할 수 있도록 설정하였다.

  해당 서비스 이용 신청을 통하여 해당 서비스를 이용 할 수 있는 Client ID 키 값과 Client Secret 키 값을 부여 받았다.



- send_naver_movie()``

```python
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
```

  project 01에서 얻은 영화명(국문)를 바탕으로 네이버 검색 API를 통해 추가적인 데이터를 수집하기 위한 코드를 작성하기에 앞서 보다 간편한 코드 작성을 위하여 위와 같이 함수를 정의 하였다. 데이터 요청을 영화명을 통해 하기 위해 매개변수로 ``movie_name`` 으로 하였다.

  보안을 위해 각각의 API 키 값은 ``.config`` 파일에`` NAVER_CLIENT_ID``, ``NAVER_CLIENT_SECRET`` 로 저장하였다. 그리고 해당 값을 ``naver_client_id`` 와 ``naver_client_secret`` 이라는 변수로 설정하여 활용하였다.

  ``BASE_URL`` 값으로 영화 검색 주소를 설정하고, ``URL`` 값을 ``BASE_URL + '?query=' + movie_name`` 으로 설정하여 ``movie_name`` 에 영화이름을 입력하였을 때 해당 영화를 검색한 결과가 나올 수 있도록 하였다.

  위 항목들의 조합을 통해 완성된 함수 ``send_naver_movie()`` 에 영화 '알라딘'을  넣었을 때 얻을 수 있는 결과의 예시는 다음과 같다.

![image-20190728213757124](/Users/Hee/Library/Application Support/typora-user-images/image-20190728213757124.png)



- ``send_naver_movie_img()``

  다음 함수 ``send_naver_movie_img()`` 는 위에서 얻은 결과 가운데 영화의 대표 이미지를 얻을 수 있는 링크 주소를 수집하기 위하여 정의하였다.

```python
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
```

  위의 예시 결과와 같이 검색 결과에 여러 영화나 검색 될 때 가장 위에 검색된 결과를 가져오기로 정하였다.

  딕셔너리 타입의 검색 결과 가운데 'items' 를 key 값으로 갖는 value 값들 가운데 가장 먼저 나오는 영화 정보 중에서 'image' 데이터를 가져오기 위해 ``send_naver_movie()`` 의 return 값 뒤 ``['items'][0]['image']`` 를 붙여 준 값을 해당 함수의 return 값으로 설정 하였다.





## movie_naver.py

  위에서 정의된 함수를 활용하여 Project 01에서 수집한 영화 목록에 있는 영화들의 정보를 수집한다.

```python
import copy
import csv
import time
import urllib.parse as urlparse

import requests

from naver_API import send_naver_movie, send_naver_movie_img
```

  위에서 작성한 함수들을 활용하기 위해 ``from naver_API`` 를 통해 해당 함수들을 import 해주었다.

```python
movie_names = []
info_list = []
result = {}
```



-  box-office.csv 에서 영화 이름 가져오기

```python
with open('./boxoffice.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    for line in reader:
        movie_names.append(line[1])
```

  Project 01에서 작성한 파일들 가운데 box-office.csv 파일을 복사해 폴더에 붙였다.  영화 이름 정보를 따로 리스트로 만들어 활용하기 위해 비어있는 ``movie_names`` 리스트를 생성 후, box-office.csv 파일 가운데 두번째 열에 해당하는 정보를  ``movie_names`` 리스트에 넣어 준다.

   box-office.csv 파일의 경우 제일 윗줄이 header 이기 때문에 해당 줄을 제외하기 위해 ``next(reader, None)`` 을 입력해준다.

 

- 영화 정보 가져오기

```python
for movie_name in movie_names:
    time.sleep(0.5)
    
    result['title'] = movie_name
    
    u = send_naver_movie(movie_name)['items'][0]['link']
    result['movieCd'] = urlparse.parse_qs(urlparse.urlparse(u).query)['code'][0]
    
		infos = ['link', 'image', 'userRating']
    for info in infos:
        if send_naver_movie(movie_name)['items'][0][f'{info}']:
            result[f'{info}'] = send_naver_movie(movie_name)['items'][0][f'{info}']
    info_list.append(copy.copy(result))
```

  위에서 생성한 movie_names 리스트에 포함된 영화 들의 정보를 모두 가져 오기 위하여 for 문을 활용하여	``send_naver_movie()`` 를 수행한다.

  단, 지속적인 요청으로 naver 서버에서 접근이 거부 당할 수 있는 사태를 방지하기 위해 각각의 요청 사이에 0.5초의 시간 지연이 생기도록  `` time.sleep(0.5)`` 함수를 설정해준다.

  영화별로 영진위 영화 대표코드, 하이퍼 텍스트 링크, 영화 썸네일 이미지의 URL, 유저 평점 등을 각각 'title', 'movieCd', 'link', 'image', 'userRating' 을 key 값으로 갖도록  비어있는 result 딕셔너리를 생성 후 , 해당 정보가 result 딕셔너리에 들어 갈 수 있게 ``copy.copy(result)`` 를 이용하였다. 

  보다 편한 정보 열람을 위해 영화 제목을 'title' 값에 넣어 주었다.

  영진위 영화 대표코드의 경우 영화 검색 결과에 나타지 않았다. 해당 정보는 Project 01의 box-office.csv 파일에 저장이 되어 있기 때문에 원하는 정보를 그냥 가져오면 되겠지만,  명세에 나타난 대로 영화 이름으로 검색한 결과만을 이용하여 정보를 가져올 수 있도록 설정하였다.  아래의 검색 결과에서 영화 코드가 나오는 곳은 하이퍼 링크 주소 끝 ``code=`` 부분이다. 

![image-20190728231034796](/Users/Hee/Library/Application Support/typora-user-images/image-20190728231034796.png)

해당 링크를 가져온 결과를 ``u`` 로 설정하고, 해당 결과 값에서 'code=' 뒷 부분만 가져오기 위해 ``urlparse.parse_qs(urlparse.urlparse(u).query)['code'][0]`` 함수를 구글링을 통해 찾아와 사용하였다. 

  나머지 정보들의 경우 for 문을 활용하여 result 값에 저장한다.

  해당 result 값은 비어있는 info_list 에 추가될 수 있도록 ``.append`` 함수를 이용하였다.



- movie_naver.csv 작성하기

```python
with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'title', 'link', 'image', 'userRating']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for result_info in info_list:
        writer.writerow(result_info)
```

  위에서 모은 info_list 내 정보들을 csv 파일로 작성하기 위해 위와 같이 코드를 작성하였다. 해당 파일의 결과물은 다음과 같다.

![movie_naver.csv_img](/Users/Hee/study_sw/submission/projects/pjt02/movie_naver.csv_img.png)

## movie_image.py 

```python
import copy
import csv
import time

import requests

from naver_API import send_naver_movie, send_naver_movie_img
```

- 영화코드, 이미지 url 정보 가져오기

  위의 movie_naver.py 파일을 통해 작성된 movie_naver.csv 파일에서 영화 코드를 key 값으로 갖고, 이미지 URL을 value 값으로 갖는 result 딕셔너리로 작성한다. 여기서 ``send_naver_movie`` 함수를 이용하여 해당 값들을 수집하여 movie_naver.csv과는 독립적인 파일을 생성할 수 도 있지만 , 정보 수집에 시간이 너무 오래 걸리기 때문에 이번 파일에서는 movie_naver.csv 파일을 이용하였다.

```python
url_list = []

with open('movie_naver.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    for line in reader:
        result = {line[0]: line[3]}
        url_list.append(copy.copy(result))
```

- 영화 대표 이미지 수집하기

  위에서 얻은 딕셔너리의 리스트를 가지고 각 영화의 이미지를 가져올 수 있도록 코드를 작성하였다. 각각의 이미지 이름에는 영화코드를, 이미지를 가져올수 있는 이미지 url 값을 넣어주기 위하여 ``movie_code``, ``image_url`` 을 활용한 for 문을 작성하였다. 수집된 이미지들을 'images' 폴더에 저장하기 위하여 해당 경로를 설정해 주었다.

```python
for url in url_list:
    time.sleep(0.5)
    for movie_code, image_url in url.items():
        with open(f'./images/{movie_code}.jpg', 'wb') as f:
            image = requests.get(f'{image_url}', stream=True).content
            if image:
                f.write(image)
```

