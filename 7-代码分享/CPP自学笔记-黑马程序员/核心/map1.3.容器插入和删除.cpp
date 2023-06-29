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

// 插入
void test01()
{
    // 创建map容器
    map<int, int> m;

    // 插入方式一：
    m.insert(pair<int, int>(1,10));
    // 插入方式二：
    m.insert(make_pair(2,20));
    // 插入方式三：(用的少)
    m.insert(map<int, int>::value_type(3, 30));
    // 插入方式四：(不建议使用),可以利用key来访问value值，如：cout << m[4] << endl;
    m[4] = 40;

    printMap(m);

    // 删除一：删除pos迭代器所指的元素
    m.erase(m.begin());
    printMap(m);p

    // 删除二：按照key删除
    m.erase(2);
    printMap(m);

    // 删除三：区间删除
    m.erase(m.begin(), m.end());
    printMap(m);
}

int main()
{

    test01();

    return 0;
}