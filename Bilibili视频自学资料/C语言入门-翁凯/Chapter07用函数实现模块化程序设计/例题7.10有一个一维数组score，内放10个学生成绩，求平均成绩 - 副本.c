/**
 *	P194 例题7.10 有一个一维数组中放了10个学生成绩，求平均成绩
 *	(利用数组实现)
 *	notes：主要练习 数组名作为函数的实参
 *
 **/
#include <stdio.h>
int main()
{

	float score[10];
	int i;
	float average(float array[10]);
	float aver;
	printf("please enter 10 numbers:\n");

	for(i=0;i<10;i++)
	{
		scanf("%f", &score[i]);		//注意输入的是%f 不是%d
	}

	//
	aver = average(score);//把数组 作为参数传递给函数
	printf("average score is : %5.2f\n",aver);
	return 0;

}

//定义函数
float average(float array[10])
{
	//思路：先求和、再除以10
	
	int i;//定义i控制循环
	float sum = array[0];
	float aver;

	for(i=1;i<10;i++)
	{
		sum = sum + array[i];	
	}
	aver = sum/10;
	return aver;
}