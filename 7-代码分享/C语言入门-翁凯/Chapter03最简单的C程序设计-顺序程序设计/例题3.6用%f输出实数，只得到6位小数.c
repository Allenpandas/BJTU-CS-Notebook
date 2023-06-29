/**
 *	例题3.6 用%输出实数，只能得到6位小数
 *	
 * */
#include <stdio.h>

int main()
{
	double a=1.0;
	printf("%f\n",a/3);//不指定输出数据的长度时： 实数中的整数部分全部输出，小数部分输出6位。
	return 0;
}