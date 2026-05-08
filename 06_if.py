# 조건문 : if ~ elif ~ else

## 회원이면 '어서오세요' 출력
member = input("회원입니까?(예 : Y, 아니오 : N ) ")

if member == "Y" :
    print("어서오세요")
elif member == "N" :
    print("회원가입 하세요")
else :
    print("Y 또는 N 중에 입력하세요")

## 나이 입력 받아 놀이공원 입장료 출력
age = int(input("나이 입력 : "))
price = 20000

if age < 6 :
    print("입장료는 무료")
elif age < 60 :
    print("입장료는 %d원" %(price))
else:
    print("입장료는 %d원" %(price * 0.5))