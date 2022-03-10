year = 2022
month = 10
day = 29
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year,month,day+10))
#을 했을 때 위와 같이 day수가 31이 넘어가면 자동으로 month+1한뒤 8일로 표시되는 방법?

# print(type(3 > 1)) 을 해주면, <class 'bool'>이 나옵니다.
#
# 저는 True 라고 출력되는 값의 자료형이 궁금해서
#
# print(type(print(3 > 1)))을 해봤는데요,
#
# True 와
#
# <class 'NoneType'>가 나왔습니다.
#
# True는 왜 나온 것이고, Nonetype은 무엇인가요?

print(type(4/2))
#다음을 실행하면 float이 나오는 이유는?