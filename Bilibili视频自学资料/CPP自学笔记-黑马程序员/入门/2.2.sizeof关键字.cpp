#include <iostream>
using namespace std;

int main(){

    // 短整型
    short num1 = 10;
    cout << "short占用内存空间为：" << sizeof(num1) << "个字节" << endl;

    int num2 = 10;
    cout << "int占用内存空间为：" << sizeof(int) << "个字节" << endl;

    long num3 = 10;
    cout << "long占用内存空间为：" << sizeof(num3) << "个字节" << endl;

    long long num4 = 10;
    cout << "long long 占用内存空间为：" << sizeof(long long) << "个字节" << endl;

    return 0;
}