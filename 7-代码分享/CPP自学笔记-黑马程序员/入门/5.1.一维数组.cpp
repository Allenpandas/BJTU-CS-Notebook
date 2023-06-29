#include <iostream>
using namespace std;
int main()
{
  // 数组

  // 定义1：数据类型 数组名 [数组长度]
  int arr[5];
  arr[0] = 10;
  arr[1] = 20;
  arr[2] = 30;
  arr[3] = 40;
  arr[4] = 50;

  // 访问数组元素
//  cout << arr[0] << endl;

  // 定义2： 数据类型 数组名[数组长度]={值1, 值2, 值3, ……}
  // 如果初始化时没有全部填写，会用0来填补剩余数据
  int arr2[5] = {10,20,30,40,50};
//  cout << arr2[0] << endl;
//  cout << arr2[1] << endl;
//  cout << arr2[2] << endl;
//  cout << arr2[3] << endl;
//  cout << arr2[4] << endl;

//    for (int i = 0; i < 5; i++)
//    {
//        cout << arr2[i] << endl;
//    }


    // 定义3
    // 不知道数组个数不能初始化；定义数组时必须要知道数组长度
    int arr3[] = {90,80,70,60,50,40,30,20,10};
    for (int i = 0; i < 9; i++)
    {
        cout << arr3[i] << endl;
    }

}