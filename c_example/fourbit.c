#include<stdio.h>
#include<stdint.h>

int main(){
    unsigned char attr; // 8bit (= uint8_t attr , stdint.h 헤더 있을 시) 
    attr = attr ^ attr;
    attr = attr | 0b00000001;
    printf("attr: 0x%02x\n",attr);
    attr = attr | (0b00000010 + 0b00000100);
    printf("attr: 0x%02x\n",attr);
    attr = attr & (~0b00000001);
    printf("attr: 0x%02x\n",attr);
    return 0;
}