//#include <iostream>
//using namespace std;
//int main(){
//
//    // 1.出现在switch语句中
//    cout << "请选择副本难度" << endl;
//    cout << "1.普通" << endl;
//    cout << "2.中等" << endl;
//    cout << "3.困难" << endl;
//
//    // 创建用户选择的结果
//    int result = 0;
//    cin >> result;
//
//    switch(result)
//    {
//        case 1:
//            cout << "您选择的是普通难度" << endl;
//            break;
//        case 2:
//            cout << "您选择的是中等难度" << endl;
//            break;
//        case 3:
//            cout << "您选择的是困难难度" << endl;
//            break;
//        default:
//            break;
//    }
//
//    return 0;
//}




#include <iostream>
using namespace std;
int main()
{
    for(int i = 0; i < 10; i++)
    {
        //如果i等于5，退出循环
        if(i == 5){
            break;
        }
        cout << i << endl;
    }
    return 0;

}



#include <iostream>
using namespace std;
int main()
{
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (j == 5){
                break;
            }
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}