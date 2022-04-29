# pip install requests

import requests, json

key = '66764e7954696c6934346168567876'
type = 'json'
service = 'GetParkInfo'
start_index = '1'
end_index = '1000'

# ex) http://openapi.seoul.go.kr:8088/(인증키)/xml/GetParkInfo/1/5/
# url은 주문서,, url은 주문서,,
url = f'http://openapi.seoul.go.kr:8088/{key}/{type}/{service}/{start_index}/{end_index}/'



response = requests.get(url)
resopnse_json = response.json()

data_row = resopnse_json["GetParkInfo"]["row"]


def get_park_info(place_gu):
    output_data=[]
    for item in data_row:
        place = item['ADDR'] # 문자열!!
        if place_gu in place:
            new_data = {}
            new_data['PARKING_NAME'] = item['PARKING_NAME']
            new_data['ADDR']         = item['ADDR']
            new_data['RATES']         = item['RATES']
            new_data['LAT']          = item['LAT']
            new_data['LNG']          = item['LNG']
            
            output_data.append(new_data)
        
    new_response = {
        "status": 200,
        "success": True,
        "message": "주차장 데이터 조회 성공",
        "data": output_data
    }
    
    return new_response

        
# new_response = get_park_info("강서구")

# new_data_list = new_response["data"]

# print(len(new_data_list), new_data_list[5])



    

# 콘솔에 이쁘게 찍기
# pretty_json = json.dumps(resopnse_json, sort_keys=False, indent=4)
# print(pretty_json)