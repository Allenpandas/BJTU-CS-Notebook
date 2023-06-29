#include <iostream>
using namespace std;

int main(){

    // 逻辑非
    int a = 10;
    cout << !a << endl;
    cout << !!a << endl;

    // 逻辑与
    int b = 10;
    int c = 20;
    cout << (b && c) << endl;

    b = 10;
    c = 0;
    cout << (b && c) << endl;

    b = 0;
    c = 0;
    cout << (b && c) << endl;

    // 逻辑非
    int d = 10;
    int e = 20;
    cout << (d || e) << endl;

    d = 0;
    e = 20;
    cout << (d || e) << endl;

    d = 0;
    e = 0;
    cout << (d || e) << endl;


    return 0;
}