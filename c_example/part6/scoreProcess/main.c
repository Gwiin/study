//구조체를 다뤄서 파일포인터로 저장, 읽어오기, 처리를 하는 프로그램

#include "scoreProcess.h"



int main(void){


    char *finpath = "../../../../study/c_example/part6/scoreProcess/score.dat";
    char *foutpath = "../../../../study/c_example/part6/scoreProcess/score.out";
    // char *finpath = "/home/asd/0309/study/c_example/part6/scoreProcess/score.dat";
    // char *foutpath = "/home/asd/0309/study/c_example/part6/scoreProcess/score.out";
    FILE *fin  = fopen(finpath,"r");
    FILE *fout = fopen(foutpath,"w");

    int n = count_studetns(fin); // 학생 수를 세는 함수, 파일에서 학생 수를 계산하여 반환

    /*printf("처리할 학생의 수를 입력하세요: ");
    if (scanf("%d",&n)!=1)
        return 1;*/ // 학생수 직접 입력받는 부분

    if (fin == NULL || fout == NULL) 
    {
        fprintf(stderr, "파일을 열 수 없습니다.\n");
        return 1;
    }

    /*
    FILE *fin_count = fopen(finpath, "r");

    if (fin_count == NULL)
    {
        fprintf(stderr, "파일을 열 수 없습니다.\n");
        fclose(fin);
        fclose(fout);
        return 1;
    }

    n = 0;
    char name[100];
    int a, b, c;

    while (fscanf(fin_count, "%99s %d %d %d", name, &a, &b, &c) == 4) { 
        n++;
    }

    fclose(fin_count);

    if (n == 0)
    {
        fprintf(stderr, "학생 데이터가 없습니다.\n");
        fclose(fin);
        fclose(fout);
        return 1;
    }
    */ // 학생 수를 파일에서 직접 계산하는 부분, count_students 함수로 대체

    Sdata *students = (Sdata *)malloc(sizeof(Sdata) * n);
    Sdata **table = (Sdata **)malloc(sizeof(Sdata*) * n);

    if(students == NULL || table == NULL)
    {
        fprintf(stderr, "메모리 할당에 실패\n");
        return 1;
    }


    inputData(fin, students, n);
    calculateScore(students, n);
    calculateRank(students, n);
    sortPointers(students, table, n);
    printResult(fout, table, n);
    
    free(students);
    free(table);

    fclose(fin);
    fclose(fout);
    return 0;

}



