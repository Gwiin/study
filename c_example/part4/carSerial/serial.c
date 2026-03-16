

int getSerialNumber(void)
{
    static int count = 0; //정적 변수는 프로그램이 종료될 때까지 메모리에 존재
    int result = count;
    ++count;
    return result;
}
