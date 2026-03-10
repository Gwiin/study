#include <stdio.h>
#include <stdint.h>

int main(void)
{
    int num;
    printf("sizeof(char) : %ld\n", sizeof(char));
    printf("sizeof(short) : %ld\n", sizeof(short));
    printf("sizeof(int) : %ld\n", sizeof(int));
    printf("sizeof(long) : %ld\n", sizeof(long));
    printf("sizeof(float) : %ld\n", sizeof(float));
    printf("sizeof(double) : %ld\n", sizeof(double));
    printf("sizeof(num) : %ld\n", sizeof(num));
    printf("sizeof(3.141592) : %ld\n", sizeof(3.141592));
    printf("sizeof(uint32_t) : %ld\n", sizeof(uint32_t)); //unsigned(음수x) int 32bit
    return 0;
}

//c는 메모리를 다루는 언어이기때문에 sizeof는 자주 쓰인다
//sizeof : 피연산자의 크기를 바이트 단위로 알려줌 (1byte = 8bit)
//2의 보수로 음수 표현