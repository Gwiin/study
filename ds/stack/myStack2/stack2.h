#pragma once
#include <stdio.h>

#define STACKSIZE 100 

typedef struct{
    int array[STACKSIZE];
    int *tos;
} Stack;

void initStack(Stack *ps);
void push(Stack *ps, int data);
int pop(Stack *ps);
