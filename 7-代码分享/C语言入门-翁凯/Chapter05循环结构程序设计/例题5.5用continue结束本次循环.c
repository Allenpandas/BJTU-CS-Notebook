#include<stdio.h>
/*
 * 例题5.5 要求输出100~200之间的不能被3整除的数。
 **/

int main()
{
	int n;
	for(n = 100;n <= 200;n++)
	{
		if(0 == n % 3)		// %为求余运算符
		{
			continue;		// continue 意为：“继续”结束本次循环，仍旧执行后面的循环
		}
		printf("%d ", n);
	}
	printf("\n");
	return 0;
}