def create_account():
    account_number = int(input("계좌번호: "))
    name = input("이름: ")
    while 1:
        deposit = int(input("예금: "))
        if deposit <0:
            print("다시 입력하세요")
            continue
        else:
           return (account_number, name, deposit)