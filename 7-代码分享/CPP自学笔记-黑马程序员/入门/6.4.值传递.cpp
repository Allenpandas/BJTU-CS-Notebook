#include <iostream>
using namespace std;

// 定义一个函数，实现两个数字进行交换
void swap(int num1, int num2)
{
    cout << "交换前：" << endl;
    cout << "num1 = " << num1 << endl;
    cout << "num2 = " << num2 << endl;

    int temp = num1;
    num1 = num2;
    num2 = temp;

    cout << "交换后：" << endl;
    cout << "num1 = " << num1 << endl;
    cout << "num2 = " << num2 << endl;
    return;
}

int main(){

    int a = 10;
    int b = 20;

    cout << "交换前：" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    // 调用函数
    swap(a,b);

    cout << "交换后：" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    return 0;
}