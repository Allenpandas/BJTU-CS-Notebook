/*
 * 例题6.1 P144 对10个数组元素依次赋值0,1,2,3,4,5,6,7,8,9，要求按照逆序输出
 **/

#include <stdio.h>
int main()
{
	int i, a[10];
	for(i = 0;i <= 9;i++)
	{
		a[i] = i;	//a[0]是数组的第一个元素 赋值为0
	}
	

	//循环打印输出
	for(i = 9;i>= 0; i--)
	{ 
		printf("%d ", a[i]);
	}
	printf("\n");
	return 0;
}