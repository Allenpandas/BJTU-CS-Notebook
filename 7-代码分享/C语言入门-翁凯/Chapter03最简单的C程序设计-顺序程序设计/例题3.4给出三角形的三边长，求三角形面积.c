/**
 *	例题3.4 给出三角形的三边长，求三角形面积
 *	
 *	
 * */
#include <stdio.h>
#include <math.h>	//引入数学库函数(下面用到了sqrt求平方根)

int main()
{
	double a,b,c,s,area;
	a = 3.67;
	b = 5.43;
	c = 6.21;
	s = (a + b + c)/2;	//s为半周长

	area = sqrt( s *(s - a) * (s - b) * (s - c));
	printf("a = %f\tb=%f\tc=%f\n",a,b,c);			// \t 代表移动一个tab的位置（一个tab有8列）
	printf("area = %f\n", area);
	return 0;


}