# 타입 어노테이션 (annotation)
# --> 파이썬은 자료형 선언 없이 변수나 함수 사용 가능
# --> 자료형을 파악하기 어려운 경우 종종 발생
# --> 파이썬 3.5버전 이상에서 사용 가능
# --> 강제성이 없는 자료형에 관한 힌트 제공 -> 꼭 지킬 필요 X
# --> 코드 자체에도 영향 X -> 에러 발생 X

# ----------------------------------------------------------

# 일반적인 변수 선언 방법
num = 1 # int
li = [1, 2, 3, 4] # list
d = {'name':'나루토', 'age':12} # dict
print(num, li, d, sep='\n')
print(type(num), type(li), type(d), sep='\n')

print('-' * 50)
# ---------------------------------------------------------

# 어노테이션을 적용한 변수 선언 방법
# 변수이름: 자료형 = 값
num: int = 1 # 변수 이름은 num, 되도록 int형
li: list = [1, 2, 3, 4]
d: dict = {'name':'나루토', 'age':12}
print(num, li, d, sep='\n')
print(type(num), type(li), type(d), sep='\n')

print('-' * 50)
# ---------------------------------------------------------

# 일반적인 함수 정의 방법
def add(a, b):
    return a + b

result = add(1, 2) # 함수 호출
print(result)
print(type(result)) # <class 'int'>

result2 = add(1.1, 2.2)
print(result2)
print(type(result2)) # <class 'float'>

result3 = add('안녕', '하세요')
print(result3)
print(type(result3)) # <class 'str'>

result4 = add([1, 2], [3, 4])
print(result4)
print(type(result4)) # <class 'list'>

print('-' * 50)
# ---------------------------------------------------------

# 어노테이션을 적용한 함수 정의 방법
# def 함수명(매개변수: 자료형) -> 반환값의 자료형:
#   함수 본체
def sub(a: int, b: int) -> int:
    return a - b

result = sub(20, 10)
print(result)
print(type(result)) # <class 'int'>

result2 = sub(5.4, 3.1) # 에러 X
print(result2)
print(type(result2)) # <class 'float'>

# result3 = sub('안녕', '하세요') -> 자료형 에러