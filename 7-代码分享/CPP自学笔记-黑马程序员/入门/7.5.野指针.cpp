#include <iostream>
using namespace std;
int main(){

    // 野指针
    // (int *)强制类型转换，将0X1100转换成int指针类型的数据（虽然OX1100看上去像个地址，但实际上是个十六进制的数字。只有强制转换成指针类型，才说明是个地址。）
    int *p = (int *)0X1100;

    // 随便拿来一个地址就访问，是不合理的；
    cout << *p <<endl;

    return 0;
}