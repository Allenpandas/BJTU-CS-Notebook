/**
 *	c = 5/9(f - 32)
 *	c为摄氏温度
 *	f为华氏温度
 * */

#include <stdio.h>
int main()
{
	float f,c;	//定义f和c为单精度浮点型变量
	f = 64.0;
	c = (5.0/9)*(f-32);	//利用公式
	printf("f=%f,n=%f\n", f,c);
}