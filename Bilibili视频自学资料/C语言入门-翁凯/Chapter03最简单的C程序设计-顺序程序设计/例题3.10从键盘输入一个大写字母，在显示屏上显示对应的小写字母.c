/**
 *	例题3.10 从键盘输入一个大写字母，在显示屏上显示对应的小写字母
 *	
 * */
#include <stdio.h>

int main()
{
	char c1,c2;
	c1 = getchar();
	c2 = c1 + 32;
	putchar(c2);

	putchar('\n');
	return 0;
}