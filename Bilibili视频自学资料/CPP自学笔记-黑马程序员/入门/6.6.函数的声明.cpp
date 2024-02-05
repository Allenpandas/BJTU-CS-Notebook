#include <iostream>
using namespace std;

// 函数的声明
// 函数的声明没有具体的代码实现
int max(int a, int b);


int main()
{
    int a = 10;
    int b = 20;
    cout << max(a, b) << endl;
    return 0;
}


// 函数的定义
int max (int a, int b)
{
    return a > b ? a : b;
}
