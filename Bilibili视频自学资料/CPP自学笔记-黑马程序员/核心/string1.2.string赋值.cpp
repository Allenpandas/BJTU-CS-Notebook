#include <iostream>
using namespace std;
#include <string>

void test01()
{
    // 第一种方式：
    string str1;
    str1 = "hello world";
    cout << str1 << endl;

    // 第二种方式：
    string str2;
    str2 = str1;
    cout << str2 << endl;

    // 第三种方式：
    string str3;
    str3 = 'a';
    cout << str3 << endl;

    // 第四种方式：
    string str4;
    str4.assign("hello C++");
    cout << str4 << endl;

    // 第五种方式：
    string str5;
    str5.assign("hello,C++", 5); //字符串的前5个字符赋值给str5
    cout << str5 << endl;

    // 第六种方式：
    string str6;
    str6.assign(str5);
    cout << str6 << endl;

    // 第七种方式：
    string str7;
    str7.assign(3, 'w');
    cout << str7 << endl;

}


int main()
{
    test01();

    return 0;
}