#include <iostream>
using namespace std;
int main()
{
    cout << "1.xxxxxxx" << endl;
    // 跳转标记
    goto ALLENPANDAS;
    cout << "2.xxxxxxx" << endl;
    cout << "3.xxxxxxx" << endl;
    cout << "4.xxxxxxx" << endl;
    // 定义标记
    ALLENPANDAS:
    cout << "5.xxxxxxx" << endl;

    return 0;
}