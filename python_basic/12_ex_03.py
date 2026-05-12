# 9.
# 사용자 지정 함수 이용해서 커피 메뉴 및 가격 출력
def price(menu) :
    if menu == 1 :
        m = '아메리카노'
        p = 3000
    elif menu == 2 :
        m = '카페라떼'
        p = 4000
    else :
        m = '바닐라라떼'
        p = 4500
    print(f'{m}: {p:,}원') # 천 단위 구분 기호 추가

menu = int(input("메뉴선택(1:아메리카노/2:카페라떼/3:바닐라라떼) "))
price(menu)

# --

# 10.
# 람다 함수 이용해서 필터링
files = ['report.hwp', 'newJeans', 'attention.png', 'ditto.jpg', 'address.xslx']

print(list(filter(lambda x : 'jpg' in x or 'png' in x, files)))