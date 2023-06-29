#include <iostream>
using namespace std;

int main(){
    int a = 10;

    // 左侧是定义一个指针 右侧是将a的地址存到p中
    int * p = &a;

    // 64位操作系统下，不管什么数据类型，都是占8个字节
    cout << "sizeof(int *)=" << sizeof(p) << endl;
    cout << "sizeof(int *)=" << sizeof(int *) << endl;
    cout << "sizeof(int *)=" << sizeof(float *) << endl;
    cout << "sizeof(int *)=" << sizeof(double *) << endl;
    cout << "sizeof(int *)=" << sizeof(string *) << endl;

    return 0;
}