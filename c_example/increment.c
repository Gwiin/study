#include <stdio.h>

int main()
{
    int a,b;
    a=5;
    b=++a; //연산 후 대입
    printf("a: %d \t b: %d\n", a,b);

    a=5;
    b=a++; //대입 후 연산
    printf("a: %d \t b: %d\n",a,b);

    printf("a: %d \t b: %d\n", a, a++);
    printf("a: %d \t b: %d\n", a, ++a);
    return 0;
}