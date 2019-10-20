import csv
with open('movieee.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'audits', 'openDt', 'showTm', 'genres', 'directors']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    # for info in data_list:
    #     writer.writerow(info)
    