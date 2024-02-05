/**
 *	P193 例题7.9 输入10个数，输出其中值最大的元素和该数是第几个数。
 *	(利用数组实现)
 *	notes：主要联系 数组元素作为函数的实参
 *	变量：先定义后使用
 *	函数：先声明、后定义、再使用
 **/
#include <stdio.h>
int main()
{
	int i;//定义i，控制循环
	int a[10];	//定义一个整形数组
	int max(int x,int y);	//声明一个max函数
	
	int m;	//，默认最大值为数组中第一个元素
	int local;	//标记定位的变量

	printf("please enter 10 number:\n");	
	for(i=0;i<10;i++)
	{
		scanf("%d", &a[i]);		//输入10个数 给a0-a9,默认回车结束scanf输入
	}
	

	//循环遍历数组中的每个元素
	for(i=1,m = a[0],local = 0;i<10;i++)
	{

		if(max(a[i],m)> m)
		{
			m = max(a[i], m);
			local = i;
		}
	}

	printf("the largest number is %d\nthe number's location is %d\n",m,local+1);
	return 0;

}

int max(int x,int y)
{
	int m;
	if(x > y)
		m = x;
	else
		m = y;
	return m;
}