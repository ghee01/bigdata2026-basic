def calc(grade) :
    """취득학점을 점수로 변환"""
    result = 0
    if grade == 'A' :
        result = 4.5
    elif grade == 'B' :
        result = 3.0
    elif grade == 'C' :
        result = 1.5
    else :
        result = 0
    return result

li = []

while True :
    choice = int(input('1.수강 강좌 정보 입력 2.평점 평균 확인 3.졸업 여건 확인 0.종료: '))
    if choice == 0 :
        print('평점평균 계산 시스템 종료')
        break

    elif choice == 1 :
        print('\n<수강 강좌 정보 입력>')
        while True :
            sub = input('과목명(종료: 0): ')
            if sub == '0' :
                print('<수강 강좌 정보 입력 종료>\n')
                break
            count = int(input('학점 수: '))
            grade = input('취득 학점(A, B, C, F): ')
            li.append([sub, count, grade])

    elif choice == 2 :
        print('\n<수강 강좌 목록>')
        print('과목명\t학점수\t학점')
        print('-' * 20)
        for x in li :
            for y in x :
                print(y, end='\t')
            print()
        print()

        score = 0
        count_sum = 0
        for i in li : # 총 수강 학점
            count_sum += i[1]
        for i in li : # 평균 평점
            score += i[1]/count_sum * calc(i[2])
        score = round(score, 2)
        if score >= 4.00 :
            print(f'평균 평점: {score} [장학 대상자]\n')
        else :
            print(f'평균 평점: {score}\n')
    
    elif choice == 3 :
        season = int(input('총 등록 학기 수 입력: '))
        if season >= 8 :
            season_check = True
            print('졸업 학기 충족\n')
        else :
            season_check = False
            print(f'{8-season}학기 부족\n')

        credit = int(input('수강 완료 학점 수 입력: '))
        if credit >= 120 :
            credit_check = True
            print('졸업 학기 충족\n')
        else :
            credit_check = False
            print(f'{120-credit}학점 부족\n')

        score = float(input('총 평균 평점 입력: '))
        if score >= 2.5 :
            score_check = True
            print('졸업 학기 충족\n')
        else :
            score_check = False
            print(f'{2.5-score} 평균 평점 낮음\n')
        
        if season_check and credit_check and score >= 4.0 :
            print('모든 졸업 요건 충족 [졸업 장학 대상자]\n')
        elif season_check and credit_check and score_check :
            print('모든 졸업 요건 충족\n')
        else :
            print('졸업 요건 부족\n')
    else :
        print('잘못된 번호입니다. 다시 선택하세요\n')