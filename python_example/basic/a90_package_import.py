import test_package
from test_package import *
# 패키지를 불러올때 딱 한번 패키지의 __init__.py를 실행시킨다. 


def main():
    print(module_var_a)
    print(module_var_b)
    print(test_package.module_var_a)
    test_package.module_b_func()
    print(test_package.Module_A())
    
    test_package.package_func()


if __name__ == "__main__":
    main()

