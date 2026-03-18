#include "stack2.h"

//TDD (Test Driven Development) : 테스트 주도 개발
//요구 명세서 -> 요구 명세 개발자 상세 -> AI (agent 사용) -> 버그 -> AI 소통
//DDD (Domain Driven Design) : 도메인 주도 개발

int main(void){

    Stack s1, s2;
    initStack(&s1);
    initStack(&s2);

    push(&s1, 100);
    push(&s1, 200);
    push(&s1, 300);

    printf("s1 First pop() : %d\n", pop(&s1));
    printf("s1 Second pop() : %d\n", pop(&s1));
    printf("s1 Third pop() : %d\n", pop(&s1));

    push(&s2, 700);
    push(&s2, 800);
    push(&s2, 900);

    printf("s2 First pop() : %d\n", pop(&s2));
    printf("s2 Second pop() : %d\n", pop(&s2));
    printf("s2 Third pop() : %d\n", pop(&s2));

    return 0;
}


