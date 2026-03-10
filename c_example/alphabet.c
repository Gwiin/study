#include <stdio.h>
#include <stdbool.h>

int main(){
    char ch;
    printf("char를 입력: "); 
    scanf("%c",&ch);

    bool isAlphabet;
    isAlphabet = ('A' <= ch && ch <= 'Z') || ('a' <= ch && ch <= 'z'); 
    printf("%c는 %s\n",ch , isAlphabet ? "알파벳입니다" : "알파벳이 아닙니다");
    return 0;
}

