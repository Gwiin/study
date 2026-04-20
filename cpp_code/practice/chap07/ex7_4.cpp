#include <iostream>
using namespace std;

class Power
{
private:
    int kick;
    int punch;
public:
    Power(int kick = 0, int punch = 0);
    ~Power();

    void show();
    Power operator+(Power op2);
    bool operator==(Power op2);
    Power &operator+=(Power op2);
};

Power::Power(int kick, int punch)
{
    this->kick = kick;
    this->punch = punch;
}

Power::~Power()
{
}

void Power::show() {
    cout << "kick = " << kick << ',' << " punch = " << punch << endl;
}

Power Power::operator+(Power op2){
    Power tmp;
    tmp.kick = this->kick + op2.kick;
    tmp.punch = this->punch + op2.punch;
    return tmp;
}

bool Power::operator==(Power op2){
    if(this->kick==op2.kick && this->punch == op2.punch)
        return true;
    else
        return false;
}

Power &Power::operator+=(Power op2){
    this->kick = this->kick + op2.kick;
    this->punch = this->punch + op2.punch;
    return *this;
}



int main(void){
    Power a(3,5), b(4,6), c;
    c = a + b;
    a.show();
    b.show();
    c.show();
    if(a==b) cout << "두 파워가 같다" << endl;
    else cout << "두 파워가 다르다" << endl;
    c += a;
    c.show();

    return 0;
}