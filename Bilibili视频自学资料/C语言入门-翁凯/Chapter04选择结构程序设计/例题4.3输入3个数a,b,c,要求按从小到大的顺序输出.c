/*
 * 例题4.3 输入3个数a,b,c 要求按照从小到达的顺序输出
 **/
#include <stdio.h>
int main()
{
	float a,b,c,t;//t负责当中间的变量
	scanf("%f,%f,%f", &a, &b, &c);

	if(a > b)
	{
		t = a;
		a = b;
		b = t;
	}
	// 第一步保证了 a < b

	if(a > c)
	{
		t = a;
		a = c;
		c = t;
	}
	// 第二步保证了 a < c	
	
	if(b > c)
	{
		t = b;
		b = c;
		c = t;
	}
	// 第三步保证了 b < c
	
	// 综上 a < b < c
	printf("%5.2f, %5.2f, %5.2f\n", a, b, c);
}