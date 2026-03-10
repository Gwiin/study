#include<stdio.h>
#include<stdint.h>
#define Bold 0x01
#define ITALIC (0x01 << 1)
#define SHADOW (0x01 << 2)
#define UNDERLINE (0x01 << 3)

int main(){
    unsigned char attr; // 8bit (= uint8_t attr , stdint.h 헤더 있을 시)
    attr = attr ^ attr;
    attr = attr | Bold;
    printf("attr: 0x%02x\n",attr);
    attr = attr | (ITALIC + SHADOW);
    printf("attr: 0x%02x\n",attr);
    attr = attr & (~Bold);
    printf("attr: 0x%02x\n",attr);
    
    if(attr & Bold)
        printf("Bold 옵션은 활성화 되었습니다.");
    else
        printf("Bold 옵션이 비활성화 되었습니다.");

    if((attr & ITALIC) >>1 )
        printf("ITALIC 옵션은 활성화 되었습니다.");
    else
        printf("ITALIC 옵션이 비활성화 되었습니다.");

    return 0;
}