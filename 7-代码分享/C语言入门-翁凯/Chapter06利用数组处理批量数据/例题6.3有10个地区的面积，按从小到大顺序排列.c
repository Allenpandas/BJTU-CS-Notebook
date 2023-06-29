/*
 * 例题6.3 P147 从小到大排序（起泡法）
 **/

#include <stdio.h>
int main()
{
	int a[10];
	int i,j,t;
	printf("intput 10 number: \n");

	for(i=0;i<10;i++)
	{
		//循环控制对数组每个元素的赋值
		scanf("%d", &a[i]);
	}
	printf("\n");

	
	for(j=0;j<9;j++){			//外循环进行n-1,即进行9次循环，实现9趟比较
		for(i=0;i<9-j;j++)		//内循环，每次进行遍历对比，把最大的依次往后排
		{
			if(a[i]>a[i+1])
			{
				t		=	a[i];
				a[i]	=	a[i+1];
				a[i+1]	=	t;	
				//比较、利用中间变量t交换位置
			}
		}	
	}
	printf("the sorted numbers : \n");
	for(i=0;i<10;i++)			//循环输出
	{
		printf("%d", a[i]);
	}
	printf("\n");
	return 0;

}
