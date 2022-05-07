import requests

# 서울 열린데이터광장 페이지 참조) 원하는 데이터의 open api 부분을 확인하여 url을 형식대로 작성
# url은 주문서,, url은 주문서,,
url = 'http://openapi.seoul.go.kr:8088/66764e7954696c6934346168567876/json/GetParkInfo/1/1000/'

# requests.get 이라는 메소드를 통해 본 url의 output인 response를 받아옴!
response = requests.get(url)

# response를 우리가 원하는 json 형태로
response_json = response.json()

# 웹을 통해 요청한 데이터 형태를 거시적으로 보고 원하는 데이터 접근(data_row 는 list 형태)
data_row = response_json["GetParkInfo"]["row"]

# 전체 데이터(data_row)에서 원하는 데이터를 new_data 에 넣는다!!
def get_data(gu):
    new_data = []
    for item in data_row:
        place = item["ADDR"]        # ex) place = "노원구~~", ["ADDR"] 키의 value값으로 주소가 있음을 미리 확인
        if gu in place:             # place에 원하는 gu 가 포함되어 있다면~
            new_data.append(item)   # new_data에 넣는다!
            
    return new_data                 # new_data를 주는 함수


# 작성한 함수는 import_api.py 에서 import하여 사용!!
        