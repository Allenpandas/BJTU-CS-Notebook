#include <iostream>
using  namespace std;

void swap(int a, int b)
{
    int temp = a;
    a = b;
    b = temp;
}

void swap2(int *p1, int *p2)
{
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

int main()
{

    // 1.值传递
    int a = 10;
    int b = 20;
    swap(a, b);
    cout << "调用swap函数之后，a的值为:" << a << endl;
    cout << "调用swap函数之后，b的值为:" << b << endl;


    swap2(&a , &b);
    cout << "调用swap2函数之后，a的值为:" << a << endl;
    cout << "调用swap2函数之后，b的值为:" << b << endl;

    return 0;
}