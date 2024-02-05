/**
 *	例题7.1用函数调用实现输出字符串
 *			******************
 *			  How do you do !
 *			******************
 **/

#include <stdio.h>
int main()
{
	void printf_star();		//声明函数 打印星星
	void printf_message();	//声明函数 打印提示消息

	//调用
	printf_star();
	printf_message();
	printf_star();

	return 0;
}


//定义函数
void printf_star()
{
	printf("*****************\n");
}

// 定义函数
void printf_message()
{
	printf(" How do you do !\n");
}