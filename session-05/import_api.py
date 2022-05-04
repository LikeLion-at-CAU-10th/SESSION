# 경로에서 아까 만든 get_data 함수 불러오기!!
from data_api_1 import get_data             # 

# 싸가지 없는 변수 선언
# 이전에 만든 get_data라는 함수의 output을 new_data에 할당!
new_data = get_data("강서구")

# 콘솔에 첫번째 데이터 찍어보기
print(new_data[0])