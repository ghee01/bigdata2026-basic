# 반복문 : for
## for와 리스트
li = ['나루토', '사스케', '사쿠라', '사이', '카카시']
for i in li :
    print(i)
print()

##for와 딕셔너리
menu = {'김밥':3000, '라면':5000, '떡볶이':4000}
for m in menu :
    print(m, end="\t") # key 출력
    print(menu[m]) # value 출력

for k, v in menu.items() : # 튜플의 언패킹 활용
    print(f'key : {k}\tvalue : {v}')
print()

## 구구단 짝수 단만 출력
for i in range(2, 10, 2) :
    print("%d단" %(i))
    for j in range(1, 10) :
        print("%d X %d = %d" %(i, j, i * j))
    print()