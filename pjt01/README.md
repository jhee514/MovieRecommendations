# Project01

  Project 01은 영화진흥위원회 오픈 API를 활용하여 지난 50주 기간의 주간 박스오피스 tOP 10 결과와 해당 영화들에 대한 상세 정보, 해당 영화 감독에 대한 상세 정보를 수집한다.

## 01.py



```python
import copy
import csv
from datetime import datetime, timedelta

import requests
from decouple import config
```

- 영화진흥위원회 API 활용

```python
API_KEY = config('API_KEY')
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={API_KEY}&weekGb=0&targetDt='
```

  영화진흥위원회 API 활용을 위해 발급받은 key값을 ``.config`` 파일에 저장해주고 decouple pip을 이용하여 해당 파일에서 활용한다. 정보 검생 url에 해당 키값이 필요함으로 f string을 이용하여 URL 값을 설정한다.



- 지난 50주간 TOP 10 영화 정보 수집

```python
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
```

  한 주간의 TOP 10 영화 목록 정보를 ``data`` 값으로 설정해준다. 위에서 설정한 URL 값에 각 날짜를 붙여 url 주소를 완성 후, requests 기능을 이용하여 정보를 가져온다.

  이 때 날짜를 파일 작성 날인 2019년 7월 13일 부터 지난 50주 간의 정보를 수집하기 위해 timedelta 기능을 for 문을 통해 활용한다.

  위와 같은 조건으로 수집한 정보들 가운데 필요한 정보(영화코드, 영화이름, 누적관객수)를 result 값에 넣어 선정해온다. 

  단 , 이 때 여러주에 걸쳐 TOP 10에 오른 영화의 경우 가장 최신 정보만을 가져오기 위하여 if 문을 활용하였다.

  모든 result 값을 저장하는 top_10 리스트 작성할 때 영화 코드만 따로 모아놓은 cd_list 리스트를 작성한다. timedelta 기능을 활용하여 최신 정보부터 순차적으로 수집할 것이기 때문에 각각 영화 코드가 cd_list 에 포함되지 않을 경우만 해당 정보를 가져오도록 ``if not movie['movieCd'] in cd_list:`` 작성한다. 



- boxoffice.csv 파일 작성

 ```python
with open ('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'movieNm', 'audiAcc']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for movie in top_10:
        if movie:
            writer.writerow(movie)
 ```

  각각의 항목이 파일 header로 올 수 있도록 fieldnames를 설정해준다.

  해당 파일의 결과물은 다음과 같다.

![](/Users/Hee/study_sw/submission/projects/pjt02/movie_naver.csv_img.png)

## 02.py

- TOP 10 영화 상세정보 수집

```python
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
```

  위에서 작성한 boxoffice.csv 파일에서 영화코드에 해당하는 첫번째 열에 해당하는 키값을 가져와 URL 에 덧붙여 해당 영화의 상세 정보를 수집할 수 있도록 data 값을 설정한다.

  영화코드, 영화이름, 영화영문이름, 영화원문이름, 누적관객수, 영화개봉일, 상영시간, 장르, 감독 정보를 모두 가져오기 위하여 각각의 값을 비어있는 result 딕셔너리에 저장하고, ``copy.copy(result)`` 를 통해 data_list 에 모두 저장한다.

  이 때, 누적관객수, 장르, 감독 같은 항목들의 경우 다른 항목들과 같은 조건으로 가져올 경우 여러 결과가 나와 정보 수집이 되지 않기 때문에 따로 추가적인 설정을 해야 한다.

- movie.csv 파일 작성

```python
with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'audits', 'openDt', 'showTm', 'genres', 'directors']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for info in data_list:
        writer.writerow(info)
```

  위에서 가져온 정보를 바탕으로 .csv 파일을 작성한다. 그 결과물은 다음과 같다.

![movei.csv_img](/Users/Hee/study_sw/submission/projects/pjt01/movei.csv_img.png)

## 03.py

- 영화 감독 상세 정보 수집

```python
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
```

  02.py 파일을 통해 얻은 movie.csv 파일을 활용하여 각각의 영화 감독 이름을 가져온다. 해당 이름을 검색URL에 붙여 상세 정보를 검색한다.

  혹시 검색하고 싶은 감독 정보가 없을 경우 코드 에러가 나지 않도록 ``if data['peopleListResult']['peopleList']:`` 문을 작성하여 원하는 정보가 존재 할 경우에만 정보를 수집할 수 있도록 설정한다.

  이 때 가져온 정보를 리스트 data_list에 더해주면서, 감독 이름만 따로 리스트 directors에 넣어 준다. 그리고 각각의 영화 정보를 가져 올 때 중복된 감독의 정보를 거르기 위해 해당 이름이 리스트 directors에 있는지 확인부터 할 수 있도록 ``if not data['peopleListResult']['peopleList'][0]['peopleNm'] in directors:`` 문을 작성한다.



- directors.csv 작성

```python
with open ('director.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['peopleCd', 'peopleNm', 'repRoleNm', 'filmoNames']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for profile in data_list:
        writer.writerow(profile)
```

  위에서 수집한 정보들을 csv 파일 형식으로 저장한다. 그 결과는 다음과 같다.

![directors.csv_img](/Users/Hee/study_sw/submission/projects/pjt01/directors.csv_img.png)