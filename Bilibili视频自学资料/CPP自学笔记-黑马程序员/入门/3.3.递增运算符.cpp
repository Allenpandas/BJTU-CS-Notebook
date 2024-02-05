#include <iostream>
using namespace std;

int main(){

    int a = 10;
    ++a;
    cout << "a=" << a << endl;

    int a2 = 10;
    int b2 = ++a2 * 10;
    cout << "b2=" << b2 << endl; // 输出110

    int a3 = 10;
    int b3 = a3++ * 10;
    cout << "b3=" << b3 << endl; // 输出100

    return 0;
}