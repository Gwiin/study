import math

class NagativeError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.args = ["이것은 내가 만든 네가티브 에러이다."]

def main():
    # input 함수는 무조건 str을 반환
    user_input = input("정수 입력")
    try:
        number_input = int(user_input)
        if number_input < 0:
            raise   NagativeError
        print("원의 반지름: ", number_input)
        print("원의 둘레: ", 2*math.pi*number_input)
        print("원의 넓이: ", math.pi*number_input*number_input)
    # except Exception as e:
    except ValueError as e:
        print("정수를 입력하지 않았습니다.\n", e)
    except NagativeError as e:
        print("양의 정수를 입력하세요.\n", e)
    finally:
        print("--------------- 프로그램이 끝났습니다. ------------------")

if __name__ == "__main__":
    main()