/**
 * P8 例题1.3 求两个整数中较大者
 * */

#include <stdio.h>
// 主函数
int main()
{
	int a, b, c;				// 定义a,b,c三个变量:其中a,b为输入变量，c为两个最大值
	int max(int x, int y);		// 声明max函数
	scanf("%d,%d", &a, &b);		// 输入a,b两个变量(scanf函数中逗号还是空格，必须与输入保持一致)
	c = max(a, b);				// 调用max函数
	printf("a和b中的最大值为%d\n", c);

}

// 定义max函数
int max(int x, int y)			// 自定义的max函数，需要传入2个形式参数int x 和 int y
{
	int max;					// 定义变量max作为做大值
	if(x > y)
		 max = x;
	else max = y;
	return max;
}