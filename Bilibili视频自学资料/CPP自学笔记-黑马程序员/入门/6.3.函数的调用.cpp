#include <iostream>
using namespace std;

// 加法函数定义
int add(int x, int y)
{
    int sum = x + y;
    return sum;
}

int main()
{
    int a = 10;
    int b = 20;

    // 函数的调用
    int c = add(a, b);
    cout << "c=" << c << endl;

    a = 500;
    b = 600;
    // 再次调用
    c = add(a, b);
    cout << "c=" << c << endl;

    return 0;
}