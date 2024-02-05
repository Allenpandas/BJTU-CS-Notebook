#include <iostream>
using namespace std;

#include <string>

void test01()
{
    // 第一种：默认构造
    string s1;

    // 第二种：
    const char * str = "hello world"; // c语言风格的字符串
    string s2(str);
    cout << "s2=" << s2 << endl;

    // 第三种：拷贝构造
    string s3(s2);
    cout << "s3=" << s3 << endl;

    // 第四种：字符串里有10个a
    string s4(10, 'a');
    cout << "s4=" << s4 << endl;
}


int main()
{

    test01();

    return 0;
}