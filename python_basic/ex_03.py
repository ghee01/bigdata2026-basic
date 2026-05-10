month = int(input("월 입력 : "))

if month >= 3 and month <= 5 :
    season = "봄"
elif month >= 6 and month <= 8 :
    season = "여름"
elif month >= 9 and month <= 11 :
    season = "가을"
else :
    season = "겨울"

print("%d월은 %s" %(month, season))