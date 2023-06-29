#include <iostream>
using namespace std;
#include <string>

void test01()
{
    string str1 = "hello";
    string str2 = "hello";

    if(str1.compare(str2) == 0)
    {
        cout << "str1 等于 str2" << endl;
    }

    string str3 = "xello";
    if(str2.compare(str3) > 0)
    {
        cout << "str2 大于 str3" << endl;
    }
    else
    {
        cout << "str2 小于 str3" << endl;
    }
}


int main()
{
    test01();

    return 0;
}