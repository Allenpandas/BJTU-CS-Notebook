#include <iostream>
using namespace std;

#include<vector>

// vector 容器的容量和大小操作


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
    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
    }

    printVector(v1);

    if (v1.empty()) // 为真 代表容器为空
    {
        cout << "v1为空" << endl;
    }else{
        cout << "v1不为空" << endl;
        cout << "v1的容量为:" << v1.capacity() << endl;
        cout << "v1的大小为:" << v1.size() << endl;
    }

    // 重新指定大小
//    v1.resize(15);
//    printVector(v1); // 如果重新指定的比原来长了，用0来填充
    v1.resize(15, 222);  //用222来填充
    printVector(v1); // 如果重新指定的比原来长了，用222来填充

    v1.resize(5);
    printVector(v1);// 如果重新指定的比原来短了，超出的部分被截断


}


int main()
{

    test01();

    return 0;
}