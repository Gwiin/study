def main():
    print("안녕하세요")
    str_var="안녕하세요"
    print(str_var[0])
    print(str_var[1])
    print(str_var[2])
    print(str_var[3])
    print(str_var[4])

    for c in str_var:
        print("for 로 불러온 원소",c)

    str_var *= 3
    print(str_var[5:10])
    print(str_var[-3:])
    print(str_var[5:10:2])
    print(str_var[-1::-1])
    print("str_var 길이", len(str_var))
    print("str_var 길이", str_var.__len__())

if __name__ == "__main__":
    main()


