#include <iostream>
using namespace std;
#include <string>

void test01()
{
    // 使用find查找字符串
    string str1 = "abcdefgde";
    int pos1 = str1.find("de");
    if(pos1 == -1)
    {
        cout << "未找到字符串" << endl;
    }else
    {
        cout << "pos1 = " << pos1 << endl;
    }

    // 使用rfind查找字符串
    int pos2 = str1.rfind("de");
    if(pos2 == -1)
    {
        cout << "未找到字符串" << endl;
    }else
    {
        cout << "pos2 = " << pos2 << endl;
    }

}

// 替换
void test02()
{
    string str1 = "abcdefg";
    str1.replace(1,3,"1111"); // 指定4个1，全部替换
    cout << "str1 = " << str1 << endl;

}

int main()
{
    // 字符串查找函数
    test01();

    // 字符串替换函数
    test02();
    return 0;
}