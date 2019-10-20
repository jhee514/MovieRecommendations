from decouple import config

from datetime import datetime, timedelta


key = config('API_KEY')
# .env의 해당 키값을 가져오라


d = datetime(2019, 7, 12) - timedelta(weeks=50)
print(type('d.strftime("%Y%m%d")'))
