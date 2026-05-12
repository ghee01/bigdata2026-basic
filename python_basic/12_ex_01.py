# 1.
# 정보 입력 받은 후 출력
univ = input("학교 : ")
dept = input("학과 : ")
name = input("이름 : ")
phone = input("연락처 : ")

print("%s 학생은 %s %s에 재학 중이며, 연락처는 %s입니다." %(name, univ, dept, phone))

# --

# 2.
# 출생년도 입력 받아 현재 나이 계산
name = input("이름 입력 : ")
year = int(input("출생년도 입력 : "))
age = 2026 - year + 1

print("2026년 시점, %s님의 한국 나이는 %d살입니다." %(name, age))

# --

# 3.
# 월 입력 받아 계절 출력
month = int(input("월 입력 : "))

if month >= 3 and month <= 5 :
    season = "봄"
elif month >= 6 and month <= 8 :
    season = "여름"
elif month >= 9 and month <= 11 :
    season = "가을"
else :
    season = "겨울"

print(f'{month}월은 {season}')

# --

# 4.
# 점수 입력받아 합격 여부 출력
score1 = int(input("1차 점수 입력 : "))
score2 = int(input("2차 점수 입력 : "))
avg = (score1 + score2) / 2

if avg >= 70 and score1 >= 50 and score2 >= 50 :
    print("합격")
else :
    print("불합격")