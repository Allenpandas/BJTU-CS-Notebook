#include <stdio.h>
#define SUM 100000
/*
 * 例题5.4：在全系1000学生中，征集慈善募捐，当总数达到10W元时就结束，统计此时捐款人数、以及平均每人捐款的数目。
 **/

int main()
{
	float amount,aver,total;	//total为捐款总数	amount为每次捐款的数量	aver为人均捐款数
	int i;
	for(i = 1, total=0;i<=1000;i++)
	{
		printf("please enter amount:");
		scanf("%f", &amount);
		total = total + amount;
		if(total >= SUM)break;
	}
	aver = total/i;
	printf("number = %d\naver = %10.2f\n", i, aver);
	return 0;
}