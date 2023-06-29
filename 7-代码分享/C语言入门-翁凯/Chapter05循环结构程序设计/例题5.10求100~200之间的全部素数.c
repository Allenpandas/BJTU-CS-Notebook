#include<stdio.h>
#include<math.h>
/*
 *	例题5.10：求100-200之间的全部素数 判断n~根号n之间的数能够被整除即可。（思考一下为啥是到根号n）
 *	
 **/

int main()
{
	int n, k, i, m=0;
	for(n=101;n<=200;n=n+2)
	{
		k = sqrt(n);	//取根号n	//最终k为整数 10

		for(i=2;i<=k;i++) //i从2开始到k(根号n)，逐一被n除(从2到10，逐一被101除)
		{
			if(n%i == 0)break;
		}

		if(i>=k+1)
		{
			printf("%d ",n);
			m = m + 1;
		}
		if(m%10 == 0) printf("\n");	// m控制每行的输出数
	}
	return 0;
}