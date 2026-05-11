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