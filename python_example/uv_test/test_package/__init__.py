from .module_a import module_var_a, module_a_func, Module_A
from .module_b import module_var_b, module_b_func, Module_B
# 파이썬은 상대경로를 써서 패키지 이름을 생략 가능하다.


__all__ = ["module_var_a","module_var_b"]

def package_func():
    print("이것은 패키지 함수입니다.")


# 패키지 테스트 코드
def main():
    print("test_package 패키지에서 실행되는 프린트다.")
    print(Module_A())
    print(Module_B())
    print(module_b_func())

print("test_package 패키지에서 실행되는 프린트다.")
