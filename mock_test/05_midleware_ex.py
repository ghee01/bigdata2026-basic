# 헬스장 입장 시스템

from datetime import datetime, timedelta

today = datetime.date(datetime.today())

def check_membership(date) :
    if date + timedelta(days=100) > today :
        print('[회원권확인] 입장 가능합니다')
        return True
    else :
        print('[회원권확인] 회원권이 만료되었습니다')
        return False
    
def check_locker(locker) :
    if 1 <= locker <= 50 :
        print('[락커확인] 사용 가능한 락커 번호입니다')
        return True
    else :
        print('[락커확인] 락커 번호는 1번에서 50번 사이여야 합니다')
        return False
    
def enter_gym(name, locker) :
    print(f'{name}님, {locker}번 락커를 사용하세요. 입장을 환영합니다.')

if __name__ == '__main__' :
    d = input('회원권 구매 날짜를 입력하세요 (YYYY-MM-DD) : ')
    buy_date = datetime.strptime(d, '%Y-%m-%d')
    buy_date = datetime.date(buy_date)
    locker = int(input('락커 번호를 입력하세요 : '))

    if check_membership(buy_date) and check_locker(locker) :
        name = input('이름을 입력하세요 : ')
        enter_gym(name, locker)