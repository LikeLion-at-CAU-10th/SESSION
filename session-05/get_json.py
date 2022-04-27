# 파싱

# 문자열 형태로 온 데이터를 잘 썰어서 필요한 데이터를 차곡차곡 저장한다!!
# 어떻게 저장?? -> json 형태!!
# json 타입은 웹에서 객체형태의 데이터를 주고 받을 때 많이 쓰는 형식
# 쉽게는 딕셔너리 형태로 생각해도 좋음 but 파일 확장자명이 json이 됨
# pip install requests 
# myvenv 도 할까??
# 간단 기본 문법(주요 자료형 리스트, 딕셔너리) => 내장 함수

# 데이터 구조
list_a = [1,2,3,4]
list_a.append(2)

dic_a = {}
dic_a["명준"] = "바보"


# 반복 조건문
# for item in list_a:
#     print(item)

# for i in range(5):
#     if i == 4:
#         # print(i)


# 문자열 파싱
str_a = "a, b, c, d, e"
ret = str_a.split(",")

str_num = "1 2 3 4 5"
ret2 = str_num.split()

# 문자열과 인트형 차이!!
numlist = []
for item in ret2:
    numlist.append(int(item))


numlist = list(map(int, str_num.split()))
# print(numlist)



###########################################################

# like fetch
import requests, json, pprint

# 간단한거 먼저 살펴보기
content = requests.get("https://jsonplaceholder.typicode.com/todos/1") 
content_json = json.loads(content.content)
content_json = json.dumps(content_json, sort_keys=False, indent=4)


url = "https://data.gm.go.kr/openapi/Ducklbrd?Key=1ed3d9acf9a440bdb4453b5122f5afed""&Type=json"
data = requests.get(url) 

data_json = json.loads(data.content)

pretty_json = json.dumps(data_json, sort_keys=False, indent=4)

target_data = data_json['Ducklbrd'][1]['row']

# pprint.pprint(data_json)
for dic in target_data:
    name = dic["BIZPLC_NM"]
    if name == "공때려":
        print(dic)

