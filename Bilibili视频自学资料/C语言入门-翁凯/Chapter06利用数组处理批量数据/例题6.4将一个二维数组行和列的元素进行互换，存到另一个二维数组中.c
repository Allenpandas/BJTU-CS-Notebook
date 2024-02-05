/*
 * 例题6.4将一个二维数组行和列的元素进行互换，存到另一个二维数组中
 *	a[2][3] = {1,2,3,4,5,6} => b[3][2] = {1,4,2,5,3,6}
 **/

#include <stdio.h>
int main()
{
	int a[2][3] = {1,2,3,4,5,6};
	int b[3][2], i, j;
	
	//输出A
	printf("array a: \n");
	for(i=0;i<=1;i++)		//一共2行元素
	{
		for(j=0;j<=2;j++)	//一共3列元素
		{
			printf("%5d",a[i][j]);
			b[j][i] = a[i][j];//对数组b进行赋值

		}
		printf("\n");//输出数组的一行之后打印一个换行
	}

	//输出B
	printf("array b:\n");
	for(i=0;i<=2;i++)
	{
		for(j=0;j<=1;j++)
		{
			printf("%5d",b[i][j]);
		}
		printf("\n");
	}

	return 0;

}                                                                         