#include <iostream>
using namespace std;
#include <string>

void test01()
{
    string str = "abcdefgh";

    // 获取子串
    string strSub = str.substr(1,3);
    cout << "strSub = " << strSub << endl;

}


// 实际操作
void test02()
{
    string email = "zhangsan@sina.com";

    int pos = email.find("@");

    // 截取用户名
    string userName = email.substr(0,pos);
    cout << userName << endl;

    // 截取域名
    string domain = email.substr(pos+1);
    cout << domain << endl;
}


int main()
{
//    test01();

    test02();
    return 0;
}