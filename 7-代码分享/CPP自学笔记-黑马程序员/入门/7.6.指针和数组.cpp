#include <iostream>
using  namespace std;
int main()
{

    // 利用指针访问数组中的元素
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    cout << "第一个元素为：" << arr[0] << endl;

    int * p = arr; //arr就是数组首地址

    cout << "利用指针访问的第1个元素是:" << *p << endl;

    p++ ; //让指针向后偏移4个字节
    cout << "利用指针访问的第2个元素是:" << *p << endl;

    // 利用指针访问所有元素
    int * p2 = arr;
    for (int i = 0; i < 10; i++)
    {
        cout << *p2 << endl;
        p2++;
    }

    return 0;
}