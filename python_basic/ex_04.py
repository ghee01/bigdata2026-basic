score1 = int(input("1차 점수 입력 : "))
score2 = int(input("2차 점수 입력 : "))
avg = (score1 + score2) / 2

if avg >= 70 and score1 >= 50 and score2 >= 50 :
    print("합격")
else :
    print("불합격")