# 덧셈 계산
def add(num1, num2) :
    print("계산 시작")
    return num1 + num2

a = int(input("숫자1 입력 : "))
b = int(input("숫자2 입력 : "))
result = add(a, b)

print(f'{a} + {b} = {result}')
print("계산 끝")

# 두 수를 입력받아 큰 수 결정
def max(x, y) :
    if x > y :
        return x
    else :
        return y

a = int(input("숫자1 입력 : "))
b = int(input("숫자2 입력 : "))
num = max(a, b)

print(f'{a}와 {b} 중 큰 수는 {num}입니다.')

# 3, 6, 9 게임
def game(num) :
    a = num // 10
    b = num % 10

    if a % 3 == 0 or b % 3 == 0 :
        return '짝'
    else :
        return num
    
x = int(input("숫자 : "))
print(game(x))

# return값 2개 이상
def add_sub(n1, n2) :
    return n1 + n2, n1 - n2
x, y = add_sub(200, 100)
print(x)
print(y)

# 가변 매개변수 *args
def adder(*args) : # 튜플 패킹
    total = sum(args)
    return total

result1 = adder(1, 2)
result2 = adder(1, 3, 5, 7, 9)
result3 = adder(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result1, result2, result3)

# 1부터 입력 받은 값까지 더해주는 함수
def add(x) :
    sum = 0
    for i in range(1, x+1) :
        sum += i
    return sum

num = int(input("숫자 입력 : "))
result = add(num)
print(f'1부터 {num}까지의 합은 {result}입니다.')