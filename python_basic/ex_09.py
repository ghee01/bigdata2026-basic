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