# 람다 표현식 : 익명 함수(함수 이름 X), 일회용
# <형식> lambda 매개변수들 : 식

## def 사용
def plus_five(x: int) :
    return x + 5

result = plus_five(10)
print(result)
print("-" * 20)

## lambda 사용
result_plus_five = lambda x : x + 5
print(result_plus_five(10))
print("-" * 20)

# lambda 표현식을 인수로 사용
# lambda x : x + 10
# map(함수, 시퀀스 자료형)
result = map(lambda x : x + 10, [10, 20, 30])
print(list(result))

# filter(람다 함수, 시퀀스 자료형) : True만 추출
result2 = filter(lambda x : x < 20, [10, 20, 30])
print(list(result2))