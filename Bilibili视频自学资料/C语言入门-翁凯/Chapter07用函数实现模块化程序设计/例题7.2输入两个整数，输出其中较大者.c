/**
 *	例题7.2输入两个整数，输出其中较大者
 **/

#include <stdio.h>
int main()
{
	int a,b,c;
	int max(int x, int y);// 声明函数的时候 不要忘记把入参也给声明了
	scanf("%d,%d", &a, &b);

	c = max(a,b);

	printf("max is %d\n", c);
	return 0;
}


int max(int x, int y)
{
	int z;
	if(x > y)
	{
		z = x;
	}else{
		z = y;
	}
	return (z);
}