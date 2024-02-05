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

// 查找和统计
void test01()
{
    // 创建map容器
    map<int, int> m;

    // 插入数据：
    m.insert(pair<int, int>(1,10));
    m.insert(pair<int, int>(2,20));
    m.insert(pair<int, int>(3,30));

    // 查找
    map<int, int>::iterator pos = m.find(3);//不管查到没查到，都会返回一个迭代器
    if(pos != m.end())
    {
        cout << "查到了元素" << (*pos).first << ",value=" << pos->second << endl;
    }else{
        cout << "未找到元素" << endl;
    }

    // 统计
    int num = m.count(3);
    cout << "num = " << num << endl;
}

int main()
{
    test01();

    return 0;
}