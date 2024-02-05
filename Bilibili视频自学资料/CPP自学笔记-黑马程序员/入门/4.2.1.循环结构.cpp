#include <iostream>
using namespace std;
int main(){
    int num = 0;
    // while填入循环条件
    // 注意事项：在写循环时，一定避免死循环
    while(num < 10){
        cout << num << endl;
        num++;
    }
    return 0;
}




#include <iostream>
using namespace std;
// time系统时间头文件包含
#include <ctime>
int main(){
    // 随机生成一个1-100之间的数字让玩家进行猜测，如果猜测，提示玩家数字过大或者过小，如果猜对了则恭喜玩家胜利，并且退出游戏。

    // 添加随机数种子，利用当前系统时间生成随机数，防止每次随机数都一样
    srand((unsigned int) time(NULL));

    // 1.生成一个随机数
//    rand() %100 // 生成0-99的随机数
    int num = rand() %100 + 1;
//    cout << "num=" << num << endl;

    // 2.让玩家进行猜测
    int value = 0;

    while(1){
        cin >> value;

        // 3.判断玩家的猜测,猜对了提示猜的结果；
        if (value > num){
            cout << "猜测过大" << endl;
        }else if (value < num){
            cout << "猜测过小" << endl;
        }else{
            cout << "猜对了" << endl;
            break; // 用break退出当前循环
        }
    }

    return 0;
}