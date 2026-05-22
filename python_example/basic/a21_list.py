import datetime

def main():
    #list 선언
    list_a = [] #아래줄보다 이방식을 주로 사용
    list_b = list()
    list_c = [1, 2, 3, 4, 5, 6] # 선언과 동시에 입력

    print(list_a, list_b, list_c)
    print(type(list_a),type(list_b), type(list_c))
    ptime = datetime.datetime.now()
    list_d = [1,2,3.141582, "padak", ptime]
    print(list_d)
    print(list_d[3])
    list_d[3] = "agu"
    print(list_d[3])

    list_e = [ [1, 2, 3] , [4, 5, 6] , [7, 8, 9] ]
    print(list_e)
    print(list_e[1][1])


if __name__ == "__main__":
    main()