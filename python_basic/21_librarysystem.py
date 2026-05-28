import csv

with open('dataFile/library.csv', 'r') as f :
    buffer = csv.reader(f, delimiter=',')
    library_list = list(buffer)
    info_list = ['주소', '상세주소', '전화번호', '팩스', '홈페이지', '개관시간', '휴관일']

    while True :
        word = input('검색어 입력(종료: 0): ')
        if word == '0' :
            print('[도서관 정보 검색 시스템 종료]')
            break
        
        print(f'\n제공 정보: {info_list}')
        info = input('원하는 정보 입력: ').split()

        print('\n[도서관 정보 검색 결과]')
        print('-' * 80)

        for li in library_list :
        # li = [2020125001,서구어린이도서관,대전광역시 서구 정림동로,25 (서구어린이도서관),042-288-4830,042-288-5939,http://www.seogu.go.kr/learning/childlib,10:00~19:00,"매주 금요일, 법정공휴일"]
            if word in li[1] :
                print_buffer = [li[1]] # 출력할 정보 리스트
                for i in info :
                # i = '개관시간'
                    info_num = info_list.index(i) + 2
                    print_buffer.append(li[info_num])
                    
                print(' | '.join(print_buffer) + ' |')

        print('-' * 80 + '\n')