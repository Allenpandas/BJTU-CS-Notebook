/*
 *	例题6.5 输出3X4矩阵中最大的元素
 *	(ps:自己写的)
 **/

#include <stdio.h>
int main()
{
	int i,j,local_i, local_j,max;
	int a[3][4] = {{1,2,3,4},{9,8,7,6}, {-10,10,-5,2}};
	max = a[0][0];//默认第一个元素最大
	for(i=0;i<=2;i++) // 3行
	{
		for(j=0;j<=3;j++)// 4列
		{
			if(a[i][j] > max)
			{
				max = a[i][j];
				local_i = i;	//local_i 标记行
				local_j = j;	//local_j 标记列
			}
		}
	}
	printf("max is: %d\nrow = %d\ncolumn = %d\n",max,local_i,local_j);
	return 0;

}
