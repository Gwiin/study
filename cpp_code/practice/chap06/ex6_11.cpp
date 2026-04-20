#include <iostream>
using namespace std;

class Circle
{
private:
    static int numOfCircles;
    int radius;
public:
    double getArea(void);
    static int getNumOfCircles(void);

    Circle(int r = 1);
    ~Circle();
};

int Circle::numOfCircles = 0;

double Circle::getArea(void){
    return 3.14 * this->radius * this->radius;
}

int Circle::getNumOfCircles(void){
    return numOfCircles;
}


Circle::Circle(int r){
    this->radius = r; 
    numOfCircles++;
} 

Circle::~Circle(){
    numOfCircles--;
}


int main(void){
    Circle *p = new Circle[10];
    cout << "생존하는 원의 개수 = " << Circle::getNumOfCircles() << endl;
    delete [] p;
    cout << "생존하는 원의 개수 = " << Circle::getNumOfCircles() << endl;
    
    Circle a;
    cout << "생존하는 원의 개수 = " << Circle::getNumOfCircles() << endl;

    Circle b;
    cout << "생존하는 원의 개수 = " << Circle::getNumOfCircles() << endl;

    return 0;
}