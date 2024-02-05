#include <iostream>
using namespace std;

int main(){

    // 整型
    int a = 0;
    cout << "请给整型变量a赋值:" << endl;
    cin >> a;
    cout << "整型变量a的值为:" << a <<endl;

    // 浮点型
    float b;
    cout << "请给浮点型变量b赋值:" << endl;
    cin >> b;
    cout << "浮点型b的值为:" << b << endl;

    // 字符型
    char ch ;
    cout << "请给字符型变量ch赋值:" << endl;
    cin >> ch;
    cout << "字符型ch的值为:" << ch << endl;

    // 字符型
    string str = "hello";
    cout << "请给字符串str赋值" << endl;
    cin >> str;
    cout << "字符串str=" << str << endl;

    // 布尔型
    bool flag = true;
    cout << "请给布尔类型的flag赋值" << endl;
    cin >> flag; //非0即为真
    cout << "布尔类型的flag=" << flag << endl;

    return 0;
}