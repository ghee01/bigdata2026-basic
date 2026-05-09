# 컬렉션 자료형 - list

li = [23, 1, 50, 8, 33, 97, 33, 14, 25, 105]
li2 = list()

li.sort() # 리스트 오름차순 정렬
li.sort(reverse = True) # 리스트 내림차순 정렬
li[2] = 10 # 값 수정
print(li)
print(li[4]) # 인덱싱
print(li[1::2]) # 슬라이싱
print(li[::-1]) # 슬라이싱 - 순서 뒤집어서 출력
print(li.count(33)) # 해당 요소의 개수 반환

print()

li2.append('원피스') # 맨 뒤에 값 하나 추가
li2.append('나루토')
li2.append(100)
li2.insert(3, '블리치') # 특정 위치에 값 추가
li2.insert(4, 3.14)
li2.remove(100) # 해당 값 찾아서 삭제
li2.pop() # 가장 끝 값 삭제

print(li2)
print(li2.index('나루토')) # index 값 반환
print(len(li2)) # 리스트 요소 개수
