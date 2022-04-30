# from data_api import get_park_info

# 데이터 구조
list_a = [1,2,3,4]
list_a[0]
list_a[0] = 2
list_a.append(2)

# print(len(list_a))

dic_a = {"ddd":12, "rrr":44}
dic_a["dasfd"] = "바보"
dic_a["ddd"]

# print(dic_a.keys())
# print(dic_a.values())
# print(dic_a.items())

# for k, v in dic_a.items():
#     print(k, dic_a[k])
    

# 반복 조건문
# for asdjfals in list_a:
#     print(asdjfals)

# for i in range(5):
#     if i == 4:
#         print(i)


# 문자열 파싱
str_a = "a, b, c, d, e"
ret = str_a.split(",")

str_num = "1 2 3 4 5"
ret2 = str_num.split()

# 문자열과 인트형 차이!!
numlist = []
for item in ret2:
    if item == '2':
        numlist.append(int(item))

# print(numlist)

numlist = list(map(int, str_num.split()))
# print(numlist)


# new_response = get_park_info("강서구")

# new_data_list = new_response["data"]

# print(len(new_data_list), new_data_list[5])