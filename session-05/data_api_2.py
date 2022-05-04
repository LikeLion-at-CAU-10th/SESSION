# Version 2 조금더 활용도를 높여서!

import requests, json

# url 에 필요한 인자들을 미리 변수로 지정해줌
key = '66764e7954696c6934346168567876'
type = 'json'
service = 'GetParkInfo'
start_index = '1'
end_index = '1000'

# ex) http://openapi.seoul.go.kr:8088/(인증키)/xml/GetParkInfo/1/5/
# 파이썬에서 변수를 스트링에 넣는 방법 => F-string 참조!!
url = f'http://openapi.seoul.go.kr:8088/{key}/{type}/{service}/{start_index}/{end_index}/'

# print(url) 을 통해서 url 이 잘만들어졌는지 확인해보아요!!

response = requests.get(url)
resopnse_json = response.json()
data_row = resopnse_json["GetParkInfo"]["row"]


def get_park_info(place_gu):
    output_data=[]
    for item in data_row:
        place = item['ADDR'] 
        if place_gu in place:
            # item 안에서 필요한 정보들만 new_data{}라는 딕셔너리에 넣어서 새로운 item 모양을 만들어줌
            new_item = {}
            # new_item의 새로운 키값(왼쪽) 할당 // 기존 item의 키값 접근(오른쪽)
            # 같지만 다른 딕셔너리 접근과 할당
            new_item['PARKING_NAME'] = item['PARKING_NAME']
            new_item['ADDR']         = item['ADDR']
            new_item['RATES']         = item['RATES']
            new_item['LAT']          = item['LAT']
            new_item['LNG']          = item['LNG']
            
            # 최종 output_data 에 차곡차곡 저장
            output_data.append(new_item)
        
    # 실제 응답 방식으로 형식에 맞춰서 데이터 키 값에 우리의 output을 값으로 지정
    new_response = {
        "status": 200,
        "success": True,
        "message": "주차장 데이터 조회 성공",
        "data": output_data
    }
    
    return new_response

        




    

