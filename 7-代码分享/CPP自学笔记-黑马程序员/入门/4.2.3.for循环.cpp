//#include <iostream>
//using namespace std;
//int main(){
//
//    // for循环，从0打印到9
//    for(int i = 0; i < 10; i++){
//        cout << i << endl;
//    }
//    return 0;
//}



// 练习案例：敲桌子从1-100，如果含7或者是7的倍数，
#include <iostream>
using namespace std;
int main(){
    // 先输出1-100

    int num = 0;
    for (int i = 1; i <=100; i++){
        // 从这100个数字中找到特殊数字，改为"敲桌子"
        // 7的倍数     对7取模，% 7 == 0
        // 个位含7     %10 == 7
        // 十位含7     /10 == 7
        if (i % 7 == 0 || i % 10 == 7 || i / 10 ==7 ){
            cout << "敲桌子" << endl;
        }else{
            cout << i << endl;
        }

        num ++;
    }

    return 0;
}