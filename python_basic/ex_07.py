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