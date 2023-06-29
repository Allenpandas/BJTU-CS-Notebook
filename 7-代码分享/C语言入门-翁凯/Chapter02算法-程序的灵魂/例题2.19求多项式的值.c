/**
 * 例2.19 求多项式(1 - 1/2 + 1/3 - 1/4 + …… +1/99 -1/100)
 * */
#include <stdio.h>
int main()
{
	int sign = 1;
	double deno = 2.0, sum = 1.0, term;//定义demo, sum, term为双精度浮点型
	while(deno <=100)
	{
		sign = -sign;		//“隔行变色”隔项变正负
		term = sign/deno;	//term 代表的是正负1/n
		sum = sum + term;
		deno = deno + 1;	//deno 代表的是1,2,3,4,5,6,7……100
	}
	printf("%f\n", sum);
	// 正确答案是:0.688172

}