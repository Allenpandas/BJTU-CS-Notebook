/**
 *	例题7.6递归计算年龄
 **/

#include <stdio.h>
int main()
{
	int age;
	int ageFunction(int n);	//注意function函数和变量不能起同一个名字
	age = ageFunction(5);
	printf("NO.5 age:%d\n",age);
	return 0;
}


//定义
int ageFunction(int n)
{
	int age;
	if(n == 1)
		age = 10;
	else
		age = ageFunction(n-1) + 2;
	return age;
}