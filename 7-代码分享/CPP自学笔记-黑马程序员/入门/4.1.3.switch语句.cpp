#include <iostream>
using namespace std;
int main() {

    // 给switch语句
    // 给电影打分：
    // 10~9 经典
    // 8~7 非常好
    // 6~5 一般
    // 5分以下，烂片

    // 提示用户给电影评分
    int score;
    cout << "请给电影进行打分" << endl;
    cin >> score;

    cout << "您输入的分数为:" << score << endl;

    switch(score)
    {
        case 10:
        case 9:
            cout << "您认为是经典电影" << endl;
            break;
        case 8:
        case 7:
            cout << "您认为是非常好的电影" << endl;
            break;
        case 6:
        case 5:
            cout << "您认为是一般的电影" << endl;
            break;
        default:
            cout << "您认为是烂片" << endl;
            break;

    }
    return 0;
}