#include <iostream>
using namespace std;
int main(){
    // 利用嵌套循环打印星图
    // 打印一行星图
    // 外层执行1次，内层执行1周
    for (int i = 0; i < 10; i++){

        for(int j = 0; j < 10; j++){
            cout << "* ";
        }
        cout << endl;
    }

    return 0;
}



//案例 乘法口诀表
#include <iostream>
using namespace std;
int main(){
    for (int i = 1; i < 10; i++){

        for (int j = 1; j < 10; j++){
            if(i >= j){
                cout << j << "*" << i << "=" << i*j << "\t";
            }
        }
        cout << endl;
    }
}