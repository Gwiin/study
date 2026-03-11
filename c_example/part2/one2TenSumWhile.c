#include <stdio.h>

int main(void){

    int i=1, sum=0;
    while(i<=10){
        sum += i;
        i++;
    }
    printf("1~10의 합 : %d\n", sum);

    return 0;
}
