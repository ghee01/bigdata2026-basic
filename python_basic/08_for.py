# 단 입력받아 구구단 출력
dan = int(input("단 입력 : "))

for i in range(1,10) :
    print(f'{dan} X {i} = {dan * i}')
print()

# 구구단 전체 출력
for i in range(2,10) :
    print(i,"단")
    for j in range(1,10) :
        print(f'{i} X {j} = {i * j}')
    print()

# 김밥 배합 출력
main = ['베이컨', '크래미']
side = ['당근', '오이']
x = 1

for m in main :
    for s in side :
        print(f'{x}: {m} + {s} + 계란')
        x += 1