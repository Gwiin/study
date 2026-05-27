import cpp_hello

def main():
    print(cpp_hello.add(45,34))
    a = cpp_hello.Hello("son")
    print(a.greet())

if __name__ == "__main__":
    main()