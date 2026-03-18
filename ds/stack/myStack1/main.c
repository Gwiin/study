#include "stack.h"
//전역 변수 사용, 포인터로 매개변수 넘기기
//배열의 사용 범위가 정해져 있음
//다수의 스택 운영이 불가능


int main(void){

    push(100);
    push(200);
    push(300);

    printf("First pop() : %d\n", pop()); //300
    printf("Second pop() : %d\n", pop()); //200
    printf("Third pop() : %d\n", pop()); //100
    return 0;
}


