## 데이터 구조!!

# 리스트
item_list= ["명준","원표","나예","서현", "정현"]  # 리스트 초기화
a = item_list[3]        # 리스트 접근
item_list[0] = "지원"    # 리스트 값 지정
item_list.append("영권") # 리스트 메소드 => append!


# 딕셔너리
item_dic = {"key1": 111, "key2":222}    # 딕셔너리 초기화 {key: value, ...}
a = item_dic["key2"]                    # 딕셔너리 값 접근
item_dic["key3"] = 333                  # 딕셔너리 값 추가(없는거 추가) -->> 뭔가 list의 append 느낌임,,
item_dic["key1"] = 222                  # 딕셔너리 값 지정(있는거 수정)
item_dic.keys()                         # 딕셔너리 메소드1. key값만 리스트 형태로 묶어놓음(정확히는 dict_keys자료형)
item_dic.values()                       # 딕셔너리 메소드2. value값만 리스트 형태로 묶어놓음(정확히는 dict_values자료형)
item_dic.items()           # 딕셔너리 메소드3. (key,value)묶음을 리스트 형태로 묶어놓음(정확히는 dict_items자료형)



## 반복 조건문!

# for, if
item_list = ["명준","원표","나예","서현", "정현"] # 모집단 데이터에서 
new_data = []                               # 특정한 기준으로 분류한 데이터를 모은다!!!

for item in item_list:                      # for 문을 통해 모집단 데이터를 item이라는 변수로 하나씩 접근(item에 list의 값들이 차례로 들어감)
    if item == "명준":                       # if 문을 통해 특정한 기준을 정함
        new_data.append(item)               # new_data리스트에 특정 기준으로 걸러진 item들을 append를 통해 차곡차곡 모아보자


# for, if 예제  
num_list = [1,2,3,4,5,6,7,8,9,10]           # 모집단 데이터 리스트
new_data2 =[]                               # 특정기준으로 분류된 데이터가 들어갈 리스트

for n in num_list:                          # for 문을 통해 모집단 데이터들을 하나씩 접근
    if n%2 == 0:                            # 특정 기준 : 짝수인 데이터!
        new_data2.append(n)                 # 특정 기준으로 모인 데이터를 new_data에 차곡차곡!
        

