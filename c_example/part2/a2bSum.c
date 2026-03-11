#include <stdio.h>

int main(void){

    int a,b,sum=0;
    printf("a b 입력: ");
    scanf("%d %d", &a,&b);
    
    for(int i=a;i<=b;i++){
        sum += i; //sum = sum + i
    }
    printf("%d ~ %d의 합은 %d\n",a,b,sum);

    return 0;
}

   