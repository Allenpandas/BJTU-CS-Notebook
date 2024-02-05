#include <iostream>
using namespace std;

#include<vector>

// vector 容器的插入和删除


void printVector(vector<int>&v)
{
    for (vector<int>::iterator it = v.begin(); it != v.end(); it ++)
    {
        cout << *it << "\t";
    }
    cout << endl;
}


void test01()
{
    vector<int>v1;

    for(int i = 0; i < 10; i++)
    {
        v1.push_back(i);
    }

    // 利用[]的方式访问数组中的元素
    for (int i = 0; i < v1.size(); i++)
    {
        cout << v1[i] << "\t";
    }
    cout << endl;

    // 利用at方式访问元素
    for (int i = 0; i < v1.size(); i++)
    {
        cout << v1.at(i) << "\t";
    }
    cout << endl;

    // 获取第一个元素
    cout << "第一个元素为:" << v1.front() << endl;
    cout << "最后一个元素为:" << v1.back() << endl;

}


int main()
{

    test01();

    return 0;
}