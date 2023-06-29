#include <iostream>
using namespace std;
#include <string>

void test01()
{

    // 第一种方式： 拼接字符串
    string str1 = "我";
    str1 += "爱玩游戏";
    cout << str1 << endl;

    // 第二种方式：拼接单个字符
    str1 += ',';
    cout << str1 << endl;

    // 第三种方式： 拼接已知的字符串变量
    string str2 = " example:FIFAonline和2Konline。";
    str1 += str2;
    cout << str1 << endl;

    // 第四种方式：append 拼接字符串
    string str3 = "I";
    str3.append(" love game ");
    cout << str3 << endl;

    // 第五种方式：append 拼接字符串的前n个字符
    str3.append("hahahaha",4);
    cout << str3 << endl;

    // 第六种方式：append 拼接字符串
    str3.append(str2);
    cout << str3 << endl;

    // 第七种方式：append 拼接部分字符串
    str3.append(str2,0,8);
    cout << str3 << endl;
}


int main()
{
    test01();

    return 0;
}