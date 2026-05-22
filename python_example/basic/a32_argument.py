def print_n_time(n : int, *value : str) -> str:
    #doc string 
    """_summary_
    교육용 테스트 함수
    Args:
        value (str): 출력할 메세지
        n (int): 반복 출력 횟수

    Returns:
        str: 에러 반환

    """    
    print(type(value))
    # temp1, temp2, temp3 = value
    for i in range(n):
        print(value)
        # print("first",temp1, "second",temp2,'third',temp3)
        for v in value:
            print(v,end=" ")
    return "ok",n

def main():
    return_var = print_n_time(3,'abc','def','ghi','ddd')
    print(type(return_var))
    print(*return_var)

if __name__ == "__main__":
    main()
