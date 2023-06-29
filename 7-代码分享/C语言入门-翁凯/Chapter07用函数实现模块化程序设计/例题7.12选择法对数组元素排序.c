/**
 *	P195 例题7.12选择法对数组元素排序
 *	notes：需要加强理解
 **/
#include <stdio.h>
int main()
{
	int array[10];//定义一个有10个元素的数组
	int i;//定义i控制循环
	void sort(int array[], int n);//
	for(i=0;i<5;i++)
	{
		scanf("%d", &array[i]);
	}
	sort(array,5);
	printf("the soeted array:\n");
	for(i=0;i<5;i++)
	{
		printf("%d,", array[i]);
	}
	printf("\n");
	return 0;

}

//定义选择排序函数
void sort(int array[], int n)
{
	int i;		//i控制数组的遍历
	int temp;	//临时存放变量(交换元素时使用)
	int k;
	int j;		//控制剩下的数组元素遍历
	for(i=0;i<n-1;i++)
	{
		k = i;
		
		//循环遍历i+1 ~ n 每个元素 选出最大的值 然后与 a[i]进行换位
		for(j=i+1;j<n;j++)
		{
			if(array[j] < array[k])	//遍历从j(i+1)~n 每个跟k比较 取最小的下标给k
			{
				k = j;	// k存的是最小的数的下标
			}
			
		}
		temp = array[k];
		array[k] = array[i];
		array[i] = temp;
	}
}









