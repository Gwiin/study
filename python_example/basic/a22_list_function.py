# var_a = 10

def make_20(var_a_b):
    # global var_a
    var_a_b[0] = 20

def main():
    var_a = 10
    # ...
    # global var_a
    wrapper_list = [var_a] #list로 가두어서
    make_20(wrapper_list)  #함수로 보냄 
    var_a = wrapper_list[0]
    print(var_a) # 20
    # 리스트의 이름은 값이 아니라 메모리를 다룬다.

    list_a = [1, 2, 3]
    list_b = [4, 5, 6, list_a] # 값의 복사가 아니고 메모리 참조

    print(list_b)
    list_a[2] = 30
    print(list_b)

if __name__ == "__main__":
    main()