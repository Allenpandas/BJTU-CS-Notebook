//#include <iostream>
//using namespace std;
//int main(){
//    int num = 0;
//    do
//        {
//        cout << num << endl;
//        num++;
//    }
//    while(num < 10);
//
//    return 0;
//}




#include <iostream>
using namespace std;
int main(){
    // 练习案例：水仙花数
    // 水仙花数是指一个三位数，每个位上的数字的3次幂之和等于他本身，如：153=1*1*1+5*5*5+3*3*3
    // 用do-while输出所有的水仙花数

    // 思路
    // 1.先将所有三位数输出（100~999）
    int num = 100;
    do{
        int a = 0;  // 个位
        int b = 0;  // 十位
        int c = 0;  // 百位

        // 2.找水仙花数
        // 获取个位 153%10      对数字取模与10
        // 获取十位 153/10%10   对数字先整除10，再对10取模
        // 获取百位 153/100     对100整除
        a = num % 10;
        b = num / 10 %10;
        c = num / 100;

        if(a*a*a + b*b*b + c*c*c == num){
            cout << num << endl;
        }
        num ++;
    }while(num <1000);

    return 0;
}