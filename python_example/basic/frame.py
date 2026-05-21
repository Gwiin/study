import sys

frame = sys._getframe()
print("현재 프레임:",frame)
print("코드 객체:",frame.f_code)
print("로컬 변수:", frame.f_locals)
print("전역 변수:", frame.f_globals)
print("module_frame co name:", frame.f_code.co_name)
print(locals())
print(globals())


def main():
    a = 123
    b = [3,4,5]
    main_frame = sys._getframe()
    print("main_frame co name : ", main_frame.f_code.co_name)
    print("local 변수 : ", main_frame.f_locals)
    print("global 변수 : ", main_frame.f_globals)

if __name__ == "__main__":
    main()