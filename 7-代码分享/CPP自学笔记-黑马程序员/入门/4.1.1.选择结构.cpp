//#include <iostream>
//using namespace std;
//
//int main(){
//
//    // 1.输入一个分数
//    int score = 0;
//    cout << "请输入一个分数" << endl;
//    cin >> score;
//
//    // 2.打印一个分数
//    cout << "您输入的分数是:" << score << endl;
//
//    // 3.分数判断
//    // 注意事项，if条件后面不要加分号
//    if (score > 600)
//    {
//        cout << "恭喜您考上了一本大学" << endl;
//    }
//    return 0;
//}




//#include <iostream>
//using namespace std;
//int main(){
//
//    // 1.输入考试分数
//    int score = 0;
//    cout << "请输入一个考试的分数" << endl;
//    cin >> score;
//
//    // 2.
//    cout << "您输入的分数为:" << score << endl;
//
//    // 3.
//    if (score > 600){
//        cout << "恭喜您考上了一本大学" << endl;
//    }else {
//        cout << "未考上一本大学" << endl;
//    }
//
//    return 0;
//}




//#include <iostream>
//using namespace std;
//int main(){
//    // 输入一个考试的分数
//    // >600 一本大学
//    // >500 二本大学
//    // >400 三本大学
//    // <400 未考上本科
//
//
//    // 1.用户输入分数
//    int score = 0;
//    cout << "请输入一个考试的分数" << endl;
//    cin >> score;
//
//    // 2.提示用户输入的分数
//    cout << "您输入的分数为:" << score << endl;
//
//    // 3.判断
//    // >600 一本大学
//    // >500 二本大学
//    // >400 三本大学
//    // <=400 未考上本科
//    if (score > 600){
//        cout << "恭喜您考上了一本大学" << endl;
//    }else if (score > 500) {
//        cout << "恭喜您考上了二本大学" << endl;
//    }else if (score > 400) {
//        cout << "恭喜您考上了三本大学" << endl;
//    }else{
//        cout << "未考上大学" << endl;
//    }
//    return 0;
//
//}




#include <iostream>
using namespace std;
int main(){
    // 1.输入高考分数
    int score = 0;
    cout << "请输入一个高考分数" << endl;
    cin >> score;

    // 2.显示高考分数
    cout << "您输入的高考分数为:" << score <<endl;

    // 3.>600 一本大学
        // >700 北大
        // >650 清华
        // >600 人大
    // >500 二本大学
    // >400 三本大学
    // <400 未考上本科
    if (score > 600){
        if(score > 700){
            cout << "恭喜你考上清华大学" << endl;
        }else if (score > 650){
            cout << "恭喜你考上北京大学" << endl;
        }else{
            cout << "恭喜你考上人民大学" << endl;
        }

    }else if (score > 500) {
        cout << "恭喜您考上了二本大学" << endl;
    }else if (score > 400) {
        cout << "恭喜您考上了三本大学" << endl;
    }else{
        cout << "未考上大学" << endl;
    }
    return 0;


}




#include <iostream>
using namespace std;
int main(){

    int num1 = 0;
    int num2 = 0;
    int num3 = 0;

    cout << "请输入小猪A的体重" << endl;
    cin >> num1;

    cout << "请输入小猪B的体重" << endl;
    cin >> num2;

    cout << "请输入小猪C的体重" << endl;
    cin >> num3;

    // 先判断A和B的重量
    if (num1 > num2){  // A>B

        if (num1 > num3){
            // A>C
            cout << "小猪A最重" << endl;
        }else{
            //C>A
            cout << "小猪C最重" << endl;
        }

    }else{
        // B > A
        if (num2 > num3){
            // B>C
            cout << "小猪B最重" << endl;
        }else{
            //C>B
            cout << "小猪C最重" << endl;
        }
    }


    return 0;
}

