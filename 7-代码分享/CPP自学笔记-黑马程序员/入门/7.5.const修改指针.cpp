#include <iostream>
using  namespace std;
int main()
{
    int a = 10;
    int b = 20;

    // 1.const 修饰指针： 常量指针(后面的可以修改： 指针可以修改)
    const int *p1 = &a;
    p1 = &b;
    cout << "*p1 = " << *p1 << endl;


    // 2.const 修饰常量：指针常量(后面的可以修改： 常量可以修改)
    int * const p2 = &a;
    * p2 = 30;
    cout << "*p2 = " << *p2 << endl;


    return 0;
}