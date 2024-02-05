/**
 *	例题3.5 求方程的根	
 *	
 * */
#include <stdio.h>
#include <math.h>	//引入数学库函数

int main()
{
	double a,b,c,disc,x1,x2,p,q;
	scanf("%lf%lf%lf", &a, &b, &c);	//输入变量a,b,c	,输入的时候要用换行隔开
	disc = b * b - 4 * a * c;	//求戴尔特
	p = -b/(2.0 * a);
	
	q = sqrt(disc)/(2.0 * a);
		x1 = p + q;
		x2 = p - q;
	printf("x1=%7.2f\nx2=%7.2f\n", x1, x2);
	return 0;


}