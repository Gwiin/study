#include <iostream>
using namespace std;

class Person
{
private:
    /* data */
public:
    int money;
    
    void addMoney(int money);

    static int shareMoney;
    static void addShared(int n);

    Person(/* args */);
    ~Person();
};


void Person::addMoney(int money){
    this->money += money;
}

int Person::shareMoney = 10;

void Person::addShared(int n){
    shareMoney += n; 
}

Person::Person(/* args */)
{
}

Person::~Person()
{
}


int main(void){

    Person::shareMoney = 20;

    cout << Person::shareMoney << endl;

    // Person han;
    // han.money = 100;
    // han.shareMoney = 200;
    
    // Person lee;
    // lee.money = 150;
    // lee.addMoney(200);
    // lee.addShared(200);

    return 0;
}