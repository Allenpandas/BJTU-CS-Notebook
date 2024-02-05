#include <iostream>
using namespace std;

int main(){

    int a ;
    // 1.定义一个指针
    // 指针定义语法： 数据类型 * 指针变量名;
    int * p;
    p = &a; //让指针p存储a的地址

    cout << "a的地址为：" << &a << endl;
    cout << "指针p为：" << p << endl;


    // 2.使用一个指针
    // 可以通过解引用的方式来找到指针指向的内存的数据
    // 指针 前加一个 * 代表解引用，指：找到指针指向的内存中的数据
    *p = 1000; // 变量P存放的地址的数据
    cout << "a的值为：" << a << endl;

    cout << "*p的值为：" << *(string *)p << endl;


    return 0;
}