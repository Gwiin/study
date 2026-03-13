#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<stdbool.h>
#include "baseball.h"
#define SIZE 3



int main(){

    system("clear");

    int count = 0;
    int strike, ball;
    int question[SIZE];
    int answer[SIZE];

    generate_number(question);

    while(true){
        input_number(answer);
        count++;

        if(check_result(question, answer, &strike, &ball)){
            break;
        }
        printf("\n");
        printf("%d Strike, %d Ball\n", strike, ball);
        printf("-----------------------\n");
    }
    printf("축하합니다! %d회만에 맞췄습니다.\n", count);
    return 0;
}



