# 연산자
## 산술 연산자 : +  -   *   /   %   //  **
## 대입 연산자 : =  +=  -=  *=  /=  //= %=

### 10000원짜리 지폐를 500원, 100원짜리 동전으로 교환
money = 10000
coin_500 = 10000//500
coin_100 = 10000//100

print("500원 동전 개수 :", coin_500)
print("100원 동전 개수 :", coin_100)
print()

### 구입 가능한 사탕의 수
money += 2000
print("현재 돈 :", money)

price = 450
candy = money // price

# change = money % price
money -= price * candy

print("구입한 사탕 개수 :", candy)
print("거스름돈 :", money)
print()

## 비교 연산자 : >  <   >=  <=  ==  !=
print(10 == 10)
print(10 % 2 != 0)
print()

## 논리 연산자 : and    or    not
a = 10
b = 60
c = a < b
print(a > 50 and b > 50)
print(a > 50 or b > 50)
print(not c)

## 문자열 연산자 : +    *
print("=" * 30)
head = "문자열"
tail = "연산자"
print(head + tail)
print("=" * 30)

## in 연산자
print(head in "문자열 연산자")
print(head not in "문자열 연산자")