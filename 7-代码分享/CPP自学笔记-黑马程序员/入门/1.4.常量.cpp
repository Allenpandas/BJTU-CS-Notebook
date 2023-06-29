#include <iostream>
using namespace std;


// 1.使用宏常量定义
#define Day 7


int main(){

//    Day = 8; // 会报错，常量不可修改
    cout << "一周有" << Day <<  "天" <<endl;

    // 2.const修饰的变量
    const int month = 12;
//    month = 24; // 会报错，常量不可修改

    cout << "一年有" << month << "个月" << endl;


    return 0;
}