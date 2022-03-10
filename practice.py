a = 80
b = 75
c = 55

print('홍길동 씨의 평균 점수는',(a+b+c)/3)

a2 = 13
if a2%2 == 0:
    print('짝수입니다')
else:
    print('홀수입니다')

#3
a3 = "8811201068234"
print(a3[0:6])
print(a3[6:])

# #4
pin = "881120-1068234"
if pin[7] == "1":
    print('남자입니다')
else:
    print('여자입니다')

#q5
five = "a:b:c:d"
five_result = five.replace(":","#")
print(five_result)

#6 리스트의 내장함수를 사용해 [1,3,5,4,2] > [5,4,3,2,1]
q6 = [1, 3, 5, 4, 2]
q6.sort()
q6.reverse()
print(q6)

#7
q7 = ['Life', 'is', 'too', 'short']
result = " ".join(q7)
print(result)

#q8
q8 = (1,2,3)
q8 = q8 + (4,)
print(q8)

#q9
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)     # a 리스트를 집합자료형으로 변환
b = list(aSet)    # 집합자료형을 리스트 자료형으로 다시 변환
print(b)          # [1,2,3,4,5] 출력


