def print_3_time():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

def print_n_time(value : str, n : int):
    #doc string 
    """_summary_
    교육용 테스트 함수
    Args:
        value (str): _description_
        n (int): _description_

    Returns:
        str: 에러 반환

    """    
    for i in range(n):
        print(value)
    return "ok"

def main():
    print("첫번째 함수 콜")
    print_3_time()
    print("두번째 함수 콜")
    print_3_time()
    print("세번째 함수 콜")
    print_3_time()

    print_n_time("안녕하세요",3)

if __name__ == "__main__":
    main()
