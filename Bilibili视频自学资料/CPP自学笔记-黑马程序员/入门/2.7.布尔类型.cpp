#include <iostream>
using namespace std;

int main(){

    bool flag = true;

    cout << flag << endl;

    flag = false;

    cout << flag << endl;

    cout << "布尔类型所占的内存空间：" << sizeof(bool) << "个字节" << endl;

    return 0;

}