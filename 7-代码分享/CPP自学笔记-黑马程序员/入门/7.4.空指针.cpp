#include <iostream>
using namespace std;
int main(){

    // 空指针
    // 1.空指针用于给指针变量初始化
    int * p = NULL;

    // 2.空指针是不可以进行访问的
    // 0~255之间的内存编号是系统占用的，因此不可以被访问
    *p = 100;

    return 0;
}