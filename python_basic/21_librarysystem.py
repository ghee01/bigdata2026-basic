import csv

with open('dataFile/library.csv', 'r') as f :
    buffer = csv.reader(f, delimiter=',')
    library_list = list(buffer)

    while True :
        word = input('검색어 입력(종료: 0): ')
        print()
        if word == '0' :
            print('[도서관 정보 검색 시스템 종료]')
            break

        print('[도서관 정보 검색 결과]')
        for li in library_list :
            if word in li[1] :
                print(f'{li[1]} | {li[2]} | {li[4]}')
        print('-' * 80)