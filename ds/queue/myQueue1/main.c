#include "queue.h"


//여러개의 큐를 다룰 수 없다 -> 구조체를 사용한다
//데이터의 갯수가 정해져 있다 100개 -> 동적할당으로 해결
//여러번 사용하면 데이터가 적어도 배열맥스를 넘긴다 
//큐에 데이터를 넣지않고 빼면 에러 발생 

int main(void){

    Queue q1;
    initQueue(&q1);

    push(&q1, 100);
    push(&q1,200);
    printf("First pop() : %d\n", pop(&q1));

    push(&q1, 300);
    printf("Second pop() : %d\n", pop(&q1));
    printf("Third pop() : %d\n", pop(&q1));

    return 0;
}


