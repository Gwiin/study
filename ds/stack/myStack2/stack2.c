#include "stack2.h"  

void initStack(Stack *ps)
{
    ps->tos = ps->array; //stack의 첫 번째 요소의 주소로 초기화;
}


void push(Stack *ps, int data)
{
    *(ps->tos) = data;
    ++ps->tos;
}


int pop(Stack *ps)
{   
    --(ps->tos);
    return *(ps->tos);
}
