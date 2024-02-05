/**
 *	P195 有2个班级，分别有5人和10人。调用一个average函数，分别求这两个班的学生的平均成绩
 *	(利用数组实现)
 *	notes：主要练习 数组名作为函数的实参
 *
 **/
#include<stdio.h>
int main()
{
	float score1[5]	 = {1,2,3,4,5};
	float score2[10] = {1,2,3,4,5,6,7,8,9,0};
	float average(float array[], int n); // 声明一个求平均值的函数 注意array[]形参不指定大小
	float aver1,aver2;//定义两个班的平均值

	aver1 = average(score1,5);
	aver2 = average(score2,10);
	printf("1班平均成绩为:%5.2f\n",aver1);
	printf("2班平均成绩为:%5.2f\n",aver2);
	return 0;

}

float average(float array[], int n)	
{
	int i;//定义i控制循环
	float sum = array[0],aver;//定义sum\aver分别求和、求平均值		//注意float sum 需要赋初始值
	for(i=1;i<10;i++)
	{
		sum = sum + array[i];
	}
	aver = sum/n;
	return aver;
}