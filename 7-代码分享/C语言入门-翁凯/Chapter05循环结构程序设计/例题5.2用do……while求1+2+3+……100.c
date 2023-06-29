#include <stdio.h>

/*
 * do while 先执行循环体，后判断
 **/
int main()
{
	int i = 1,sum = 0;	//i控制循环体; sum为和
	do
	{
		sum = sum + i;
		i++;
	}
	while(i <= 100);
	printf("sum = %d\n",sum);
	return 0;
}