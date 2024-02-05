/**
 *	例题3.9 从键盘输入BOY三个字符，然后把他们输出到屏幕
 *	
 * */
#include <stdio.h>

int main()
{
	char a,b,c;
	a = getchar();
	b = getchar();
	c = getchar();
	// 注意，操作的时候需要连续输入BOY，并按Enter键。 
	// 解释：在键盘输入信息时，会将字符先暂存在键盘的缓冲器中，只有按了Enter键才会一起输送到计算其中。

	putchar(a);
	putchar(b);
	putchar(c);

	putchar('\n');

	return 0;
}