# 강제종료 : ctrl + c

year = 1
while year <= 3 :
    print(f'서당개 {year}년')
    year += 1
print("풍월을 읊습니다.")
print()

result = None
while result != 'Y' :
    print("실행")
    result = input("계속하려면 입력(종료 : Y) : ")
print("종료")
print()

# 캐릭터 기본 체력 100
# 정수 데미지 입힌다 - input()
# 체력 0 되면 종료
hp = 100
while hp > 0 :
    print(f'현재 체력은 {hp}입니다.')
    damage = int(input("데미지를 얼마나 입힐까요? "))
    hp -= damage
print(f'체력이 0이 되어 종료합니다.')
print()

# 1~30 정수 중 7의 배수 출력 - continue 사용
x = 1
while x <= 30 :
    if x % 7 != 0 :
        x += 1
        continue
    print(f'7의 배수 : {x}')
    x += 1

# 0 입력 전까지 단 입력 받아 구구단 출력
while True :
    dan = int(input("단 입력(종료 0) : "))
    i = 1

    if dan == 0 :
        print("구구단 프로그램 종료")
        break

    while i <= 9 :
        print(f'{dan} X {i} = {dan * i}')
        i += 1
    print()