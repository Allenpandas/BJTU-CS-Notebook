#include <iostream>
using namespace std;

// 1.创建学生数据类型（包括：姓名、年龄、分数）
// 自定义数据类型，一些类型集合组成的一个类型
// 语法： struct 类型名称 {成员列表}
// 结构体定义的时候，struct不能省略
struct Student
{
    // 成员列表

    // 姓名
    string name;
    // 年龄
    int age;
    // 分数
    int score;
}s3;


int main()
{

    // 2.1. struct Student s1
    // 数据类型 struct Student
    // 变量名 s1
    // 结构体创建时，struct关键字可以省略
    struct Student s1;
    s1.name = "张三";
    s1.age = 18;
    s1.score = 100;
    cout << "姓名:" << s1.name << ",年龄:" << s1.age << ",分数:" << s1.score << endl;

    // 2.2. struct Student s2 = {}
    struct Student s2 = {"李四", 19, 85};
    cout << "姓名:" << s2.name << ",年龄:" << s2.age << ",分数:" << s2.score << endl;

    // 2.3. 定义结构体的时候顺便创建结构体变量(不建议使用)
    s3.name = "王五";
    s3.age = 20;
    s3.score = 60;
    cout << "姓名:" << s3.name << ",年龄:" << s3.age << ",分数:" << s3.score << endl;

    return 0;
}