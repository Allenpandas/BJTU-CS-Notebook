#include <iostream>
#include<map>
using namespace std;

void printMap(map<int, int>&m)
{
    for (map<int, int>::iterator it = m.begin(); it != m.end(); it ++)
    {
        cout << "key = " << (*it).first << ", value = " << it->second << endl;
    }
    cout << endl;
}

// 大小
void test01()
{
    // 创建map容器
    map<int, int> m;

    m.insert(pair<int, int>(1,10)); // key=1, value=10
    m.insert(pair<int, int>(2,20));
    m.insert(pair<int, int>(3,30));
    m.insert(pair<int, int>(4,40));
    printMap(m);

    if(m.empty())
    {
        cout << "m为空" << endl;
    }else{
        cout << "m不为空" << endl;
        cout << "m的大小为" << m.size() << endl;
    }
}


// 交换
void test02()
{
    // 创建mapmap容器
    map<int, int> m;

    m.insert(pair<int, int>(1,10)); // key=1, value=10
    m.insert(pair<int, int>(2,20));
    m.insert(pair<int, int>(3,30));
    printMap(m);

    // 创建map容器2
    map<int, int> m2;
    m2.insert(pair<int, int>(5,500)); // key=1, value=10
    m2.insert(pair<int, int>(6,600));
    m2.insert(pair<int, int>(7,700));
    printMap(m2);

    cout << "交换前：" << endl;
    printMap(m);
    printMap(m2);
    cout << "交换后：" << endl;
    m.swap(m2);
    printMap(m);
    printMap(m2);

}

int main()
{

//    test01();
    test02();

    return 0;
}