#include <stdio.h>
#include <stdbool.h>


int main(){
    char ch;
    printf("char를 입력하세요: ");
    scanf("%c",&ch);

    bool isBig;
    isBig = ('A' <= ch && ch <= 'Z');
    printf("%c는 %s\n",ch,isBig ? "대문자입니다." : "대문자가 아닙니다.");
    return 0;
}


