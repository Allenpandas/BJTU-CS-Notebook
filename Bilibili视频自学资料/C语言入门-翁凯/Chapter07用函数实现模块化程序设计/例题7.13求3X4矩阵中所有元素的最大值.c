/**
 *	P195 例题7.13求3X4矩阵中所有元素的最大值
 *	notes：需要加强理解
 **/
#include <stdio.h>
int main()
{
	int max;//定义最大值变量
	int max_value(int array[][4]);//声明函数
	int a[3][4] = {1,3,5,7,2,4,6,8,15,17,34,12};
	max = max_value(a);
	printf("max is : %d\n", max);
	return 0;
}



//函数逐个元素比较 没有太大难度
//notes:必须要指定列数!!!(C语言编译的时候不检查第一维的大小,检查第二维的大小)
int max_value(int array[][4])
{
	int max; //定义获取的最大值
	int i,j; //定义变量i,j控制循环,i是行;j是列
	max = array[0][0];
	for(i=0;i<3;i++)
	{
		for(j=0;j<4;j++)
		{
			if(array[i][j] > max)
				max = array[i][j];
		}
	}
	return max;
}