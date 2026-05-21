# ex6_1_python_critical_section.py  임계영역
# 공유 자원 : 은행 잔고

import threading

total_balance = 0 # 은행 잔고

def deposit(amout):
    global total_balance
    for i in range(amout): # 0 ~ amout-1
        total_balance += 1


if __name__ == "__main__":
    t1 = threading.Thread(target=deposit, args=(100000,))
    t2 = threading.Thread(target=deposit, args=(100000,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"최종 잔액 : {total_balance}원")
    print(f"최종 잔액 기대값 : 20000원")