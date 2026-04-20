#include <iostream>
using namespace std;


class Coffee
{
private:
    int water, espresso, sugar, cream;
public:
    void show(void);

    Coffee operator+(Coffee &op);
    Coffee operator+(int n);

    Coffee(int water=1, int coffee=1, int sugar=0, int cream=0);
    ~Coffee();
};

void Coffee::show(void){
    cout << "물" << water << ", 커피 " << espresso;
    cout << ", 설탕 " << sugar << ", 크림 " << cream << endl;
}

Coffee Coffee::operator+(Coffee &op){
    Coffee tmp;
    tmp.water = this->water + op.water;
    tmp.espresso = this->espresso + op.espresso;
    tmp.sugar = this->sugar + op.sugar;
    tmp.cream = this->cream + op.cream;
    return tmp;
}

Coffee Coffee::operator+(int n){
    Coffee tmp;
    tmp.water = this->water;
    tmp.espresso = this->espresso + n;
    tmp.sugar = this->sugar;
    tmp.cream = this->cream;
    return tmp;
}
 

Coffee::Coffee(int water, int coffee, int sugar, int cream){
    this->water = water;
    this->espresso = coffee;
    this->sugar = sugar;
    this->cream = cream;
}

Coffee::~Coffee(){}

int main(void){
    Coffee black(2,5,0,0), dabang(2,2,2,2), c, d;
    c = black + dabang;
    d = c + 1;
    c.show();
    d.show();

    return 0;
}
