#include<stdio.h>
#include<stdbool.h>

bool arrayCompare(int *array, int *array2, int index, int *diff);


int main(void){
    int nums1[] = {1,3,7,4,9};
    int nums2[] = {1,3,7,4,9};
    int nums3[] = {1,3,7,9,5};
    int diff =0;

    if(arrayCompare(nums1, nums2, 5,&diff)){
        printf("nums1과 nums2는 같다.\n");
    }else{
        printf("두 배열은 다르다.%d index가 다르다\n", diff);
    }
    if(arrayCompare(nums1, nums3, 5,&diff)){
        printf("nums1과 nums3는 같다.\n");
    }else{
        printf("두 배열은 다르다.%d index가 다르다\n", diff);
    }
    if(arrayCompare(nums2, nums3, 5,&diff)){
        printf("nums2과 nums3는 같다.\n");
    }else{
        printf("두 배열은 다르다.%d index가 다르다\n", diff);
    }

    return 0;
}

bool arrayCompare(int *array, int *array2, int index, int *diff){

    int i;
    for(i=0;i<index;i++){
        if(array[i] != array2[i]){
            *diff = i;
            return false;
        }
    }
    return true;
}