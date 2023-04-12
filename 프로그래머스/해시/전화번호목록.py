'''
# L2. 전화번호 목록
주어진 전화번호 중 한 전화번호가 다른 전화번호의 접두어일 경우 False를 출력하시오.
'''

def solution(phone_book):
    pb = dict()
    for phone_number in phone_book:                     # 가능한 phone_number dictionary에 추가
        pb[phone_number] = True     
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):           # 같은 전화번호 존재하지 않음
            target = phone_number[:i]                   # 가능한 접두사
            if target in pb.keys(): return False        # 해당 접두사가 dictionary에 있는지
    return True
