# 5.
# 랜덤 숫자 맞추기
from random import randint
ran_num = randint(1,30)

while True :
    user_num = int(input("숫자 입력(종료 0) : "))
    
    if ran_num == user_num :
        print("정답")
        break
    elif user_num == 0 :
        print("종료")
        break
    elif ran_num > user_num :
        print("더 큰 숫자 입력")
    else :
        print("더 작은 숫자 입력")

# --

# 6.
# 로또 번호 생성
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

## sample 이용
## sample(범위, 개수) : 범위에서 개수만큼 중복없이 숫자 추출
li2 = sample(range(1,46), 6)
print(li2)

# --

# 7.
# 랜덤 단어 타자게임
from random import choice
li = ['원피스', '나루토', '블리치', '헌터헌터', '귀멸의칼날', '주술회전', '체인소맨']

input("타자게임 시작 (엔터 입력)")
cnt = 1

while True :   
    i = choice(li) # 랜덤으로 요소 한개 선택
    str = input(f'문제{cnt} (종료 0) : {i}\n')

    if str == '0' :
        break
    elif str == i :
        print("맞음!")
    else :
        print("틀림! 다시!")
    print()

    cnt += 1

# --

# 8.
# 딕셔너리 이용해서 MT 장소 투표
mt = {'대성리':0,
      '춘천':0,
      '을왕리':0,
      '청평':0}

for key in mt :
    print(f'{key}:{mt[key]}표', end=" ")
print('\n')
print("<< MT 장소 투표 >>")

while True :
    vote = input("장소 : ")
    if not vote :
        break
    mt[vote] += 1

result = max(mt, key=mt.get) # key : 비교의 기준

for key in mt :
    print(f'{key}:{mt[key]}표', end=" ")
print('\n')
print(f'최다득표 : {result} {mt[result]}표')
