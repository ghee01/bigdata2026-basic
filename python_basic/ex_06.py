from random import randint, sample
li = []
while True :
    num = randint(1, 45)
    if num not in li :
        li.append(num) 
    if len(li) == 6 :
        break

print("<< 생성된 로또 번호 >>")
for i in li :
    print(i, end=" ")
print()

# sample 이용
# sample(범위, 개수) : 범위에서 개수만큼 중복없이 숫자 추출
li2 = sample(range(1,46), 6)
print(li2)