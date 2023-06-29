#include <iostream>
using namespace std;
#include <string>

void test01()
{
    string str = "hello";
    cout << "str = " << str << endl;

    // 方式1：通过[]访问单个字符
    for(int i = 0; i < str.size(); i++)
    {
        cout << str[i] << endl;
    }

    // 方式2：通过at访问单个字符
    for(int i = 0; i < str.size(); i++)
    {
        cout << str.at(i) << endl;
    }

    // 修改单个字符
    str[0] = 'x';
    cout << "str = " << str << endl;

    str.at(1) = 'y';
    cout << "str = " << str << endl;
}


int main()
{
    test01();

    return 0;
}