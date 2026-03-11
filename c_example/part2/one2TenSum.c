#include <stdio.h>

int main(){
    int sum=0;
    for(int i=0;i<10;++i){ //0부터 시작하는 것이 좋다 => 배열
        sum = sum + i + 1;
    }
    printf("1~10까지의 합: %d\n",sum);
    return 0;
}