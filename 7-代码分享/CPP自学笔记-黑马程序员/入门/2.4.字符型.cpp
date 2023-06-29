#include <iostream>
using namespace std;

int main(){

    char ch = 'a';

    cout << "ch=" << ch << endl;

    cout << "char类型所占内存空间为" << sizeof(char) << "个字节" << endl;

    cout << "a对应的ASCII码值为:" << (int)ch << endl;
    //小写a是97；大写A是65

    return 0;
}