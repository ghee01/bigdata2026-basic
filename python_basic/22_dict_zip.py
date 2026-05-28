# dict : 딕셔너리 자료형

# 딕셔너리 생성
d = {'a':1, 'b':2, 'c':3}
print(d)
print(type(d)) # <class 'dict'>

d2 = [('a',1), ('b',2), ('c',3)]
print(d2)
print(type(d2)) # <class 'list'>

# 딕셔너리로 형변환
d2 = dict(d2)
print(d2) # {'a':1, 'b':2, 'c':3}
print(type(d2)) # <class 'dict'>

# 또 다른 딕셔너리 생성 방법
d3 = dict(a = 1, b = 2, c = 3)
print(d3) # {'a':1, 'b':2, 'c':3}
print(type(d3)) # <class 'dict'>

# ---
print('-' * 80)
# ---

# zip() 함수
# 키는 키끼리, 값은 값끼리 묶는다 (딕셔너리)
# 같은 인덱스 번호끼리 묶는다 (리스트, 튜플)
d4 = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(d4) # {'a':1, 'b':2, 'c':3}
print(type(d4)) # <class 'dict'>

li = ['a', 'b', 'c']
tu = (1, 2, 3)
result_zip = zip(li, tu)
print(result_zip)
print(type(result_zip)) # <class 'zip'>
for i in result_zip :
    print(i)
print(list(zip(li, tu))) # 리스트로 형변환 --> [('a',1), ('b',2), ('c',3)]

li_1 = [1, 2]
li_2 = ['a', 'b', 'c', 'd']
li_3 = ['가', '나', '다']
print(list(zip(li_1, li_2, li_3))) # [(1, 'a', '가'), (2, 'b', '나')]

for i in zip(li_1, li_2, li_3) :
    print(i)

# ---
print('-' * 80)
# ---

# 튜플 언패킹
for z1, z2, z3 in zip(li_1, li_2, li_3) :
    print(f'z1: {z1}, z2: {z2}, z3: {z3}')

# ---
print('-' * 80)
# ---

# enumerate()
for index, value in enumerate(li_2) :
    print(f'index: {index}, value: {value}')
print()

for index, value in enumerate(li_2, start=1) : # index값 1부터
    print(f'index: {index}, value: {value}')

# ---
print('-' * 80)
# ---

# 딕셔너리와 for
print(d4) # {'a': 1, 'b': 2, 'c': 3}
for i in d4 :
    print(i) # key 출력
print()

for i in d4 :
    print(d4[i]) # value 출력

# ---
print('-' * 80)
# ---

# .keys()
print(d4)
for i in d4.keys() :
    print(i)

print(d4.keys()) # dict_keys(['a', 'b', 'c'])
print(list(d4.keys())) # ['a', 'b', 'c']

# ---
print('-' * 80)
# ---

# .values()
for i in d4.values() :
    print(i)

print(d4.values()) # dict_values([1, 2, 3])
print(list(d4.values())) # [1, 2, 3]

# ---
print('-' * 80)
# ---

# .items() --> (key, value)
for i in d4.items() :
    print(i)

for k, v in d4.items() : # 튜플 언패킹
    print(f'k: {k}, v: {v}')

# ---
print('-' * 80)
# ---

# 튜플 패킹 --> def func(*args)
# *args : 가변 매개변수
def func(*args) :
    total = 0
    for i in args :
        total += i
    return total

result1 = func(1, 2)
result2 = func(1, 2, 3)
result3 = func(1, 2, 3, 4, 5)
result4 = func(10, 2, 44, 21, 5, 12)

print(result1, result2, result3, result4)

# ---
print('-' * 80)
# ---

def func2(name, *args) :
    total = 0
    for i in args :
        total += i
    print(f'{name}가 더한 값은 {total}입니다')

func2('나루토', 1, 2, 3)
func2('사스케', 10, 20)