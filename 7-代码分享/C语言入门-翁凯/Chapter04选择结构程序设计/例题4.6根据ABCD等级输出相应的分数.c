#include<stdio.h>

int main()
{
	void action1(int,int),action2(int,int);//声明2个函数。 函数先声明后使用；变量先定义后使用
	
	char ch;
	int a = 15,b = 23;
	ch = getchar();//获取一个字符
	switch(ch)
	{
		case 'a':	
		case 'A':action1(a,b);break;
		case 'B':
		case 'b':action2(a,b);break;
		
		default:putchar('\a');
	}
	return 0;
}

void action1(int x,int y)
{
	printf("x+y=%d\n",x+y);
}

void action2(int x,int y)
{
	printf("x*y=%d\n",x*y);
}