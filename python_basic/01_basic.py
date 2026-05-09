# 주석
# <형식> 변수명 = 값
# 변수명 : 예약어 사용 X, 첫 글자 숫자 X

hello = "안녕하세요"
print(hello)

# 예약어 확인
import keyword
print(keyword.kwlist)
print()

# 이름, 나이 변수에 저장 후 출력
name = "나루토"
age = 12
print(name, age, sep="/")
print(name, end="/")
print(age)
print()

# 자료형
## 기본 자료형 : int, float, bool, str
##컬렉션 자료형 : list, dict, tuple, set
num = 100
print(num, type(num))

num = 95.5
print(num, type(num))

name = "사스케"
print(name, type(name))

result = True
print(result, type(result))