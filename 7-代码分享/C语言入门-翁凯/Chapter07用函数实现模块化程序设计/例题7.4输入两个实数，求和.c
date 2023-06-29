/**
 *	例题7.4输入两个实数，求和
 **/

#include <stdio.h>
int main()
{
	float a,b,sum;
	float add(float a, float b); //声明
	//注意把所有的声明，都写在最前面。

	printf("请输出两个实数，用逗号隔开\n");
	scanf("%f,%f",&a,&b);

	sum = add(a,b);
	printf("sum is : %3.2f\n", sum);
	return 0;

}

//定义函数
float add(float a,float b)
{
	float sum;
	sum = a + b;
	return sum;
}