import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
#dummy_data
dummy_data = []

# API 요청
for i in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    #dummy_data에 유저이름 추가
    if -80< lat < 80 and -80< lng < 80:
        #dummy_data에 넣을 dict 구성
        indummydic = {
            'company' : parsed_data['company']['name'],
            'lat' : parsed_data['address']['geo']['lat'], 
            'lng' :parsed_data['address']['geo']['lng'], 
            'name':parsed_data['name'] 
            }
        dummy_data.append(indummydic)
    

print(dummy_data)

