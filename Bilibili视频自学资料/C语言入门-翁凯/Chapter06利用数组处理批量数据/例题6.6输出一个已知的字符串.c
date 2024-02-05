/*
 *	例题6.6输出一个已知的字符串
 *	(题意：先定义好一整串字符，逐个输出数组中的内容)
 **/

#include <stdio.h>
int main()
{
	char c[15] = {'I',' ','a','m',' ','a',' ','s','t','u','d','e','n','t','.'};
	int i;
	for(i=0;i<15;i++)
	{
		printf("%c",c[i]);
	}
	printf("\n");
	return 0;
}
