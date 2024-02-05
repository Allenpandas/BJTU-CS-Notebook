#include <iostream>
using namespace std;

// 1.无参数，无返回值
void test01()
{
    cout << "this is test01" << endl;
}

// 2.有参数，无返回值
void test02(int a )
{
    cout << "this is test02, a = " << a << endl;
}

// 3.无参数，有返回值
int test03()
{
    cout << "this is test03" << endl;
    return 1000;
}

// 4.有参数，有返回值
int test04(int a )
{
    cout << "this is test04, a = " << a << endl;
    return a;
}


int main(){

    // 无参数，无返回值调用
    test01();
    // 有参数，无返回值调用
    test02(2);
    // 无参数，有返回值调用
    int num1 = test03();
    cout << "num1 = " << num1 << endl;
    // 有参数，有返回值
    int num2 = test04(1000);
    cout << "num2 = " << num2 << endl;

    return 0;
}