#include "stack.h"  

static int stack[50]; 
static int tos=0; //top of stack

void push(int data){
    stack[tos] = data;
    ++tos;
}

int pop(void){
    --tos;
    return stack[tos];
}