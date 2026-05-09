# 컬렉션 자료형 - dictionary

## di = {}
## di = dict()

menu = {'김밥':3000, '라면':5000}
print(menu)

print(menu['김밥']) # key로 value 찾기
print(menu['라면'])

menu['떡볶이'] = 5000 # 값 추가
menu['김밥'] = 4000 # 값 수정
print(menu)

del(menu['라면']) # key-value 쌍 삭제
print(menu)
print()


# 컬렉션 자료형 - set : 순서 없음, 중복 불가능

a = {30, 20, 10}
b = set() # 빈 세트
c = {40, 20}
print(a, c)

print(a & c) # 교집합
print(a | c) # 합집합
print(a - c)
print(c - a) # 차집합