/*
 * 例题4.4 输入一个字符，判别它是否为大写字母，如果是，将它转换成小写字母；如果不是，不转换。
 * 然后输出最后得到的字符
 **/
#include <stdio.h>
int main()
{
	char ch;	//定义变量用来存放输入的字符
	scanf("%c", &ch);	//%c
	ch = (ch >= 'A' && ch <= 'Z')?(ch+32):ch;//如果是大写字母，ASCII码+32;
	printf("%c\n", ch);
	return 0;
}