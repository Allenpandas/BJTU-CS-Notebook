#include <iostream>
using  namespace std;
int main()
{
    // continue语句
    for (int i = 0; i < 10; i++)
    {
        // 只输出奇数，不输出偶数
        if (i % 2 == 0)
        {
            continue;
        }
        cout << i << endl;
    }

    return 0;
}