/**
 *	例题7.5输出4个整数，找出其中的最大值（利用函数的嵌套）
 **/

#include <stdio.h>
int main()
{
	int a,b,c,d,max;
	int maxFunction(int a,int b,int c,int d);

	printf("请输入4个整数\n");
	scanf("%d,%d,%d,%d",&a,&b,&c,&d);
	max = maxFunction(a,b,c,d);

	printf("max is : %d\n", max);
	return 0;
}

//函数定义
int maxFunction(int a,int b,int c,int d)
{
	int max2(int a, int b);// 声明一个函数,求2者之间的最大值
	int max;
	max = max2(a,b);		//求a,b中的最大者,赋值给max
	max = max2(c,max);		//max与c进行比较,赋值给max
	max = max2(d,max);		//max与d进行比较,赋值给max
	return max;
}


int max2(int a, int b)
{
	int max;
	if(a >= b)
	{
		max = a;
	}else{
		max = b;
	}
	return max;
}