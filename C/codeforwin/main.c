#include <stdio.h>

int main()
{work10();}
// Function 1
int work1()
{
	int  i, j;
	 for (i=1; i<=5; i++)
	 {
		 for (j=1; j<=5; j++)
			 printf("1");
			puts("");
	 }
}

int work2()
{
	int i,j,x,y,r;
	
	for(r=1; r<=5; r++)
	{
	for (i=1; i<= 5; i++)
	{
		for(j=1; j<=5; j++);
		printf("1");}
		puts("");
	for (x=1; x<=5; x++)
	{
			for(y=1; y<=1;y++)
				printf("0");
		}
	puts("");
	}
}

int work3()
{
	int i,j;
	
	for(i=1; i<=5;i++)
	{
		for(j=1;j<=i; j++)
			printf("%d",i);
		puts("");
	}
}

int work4()
{
	int i,j;
	
	for(i=5; i>=1; i--)
	{
		for(j=1; j<=i; j++)
			printf("%d",i);
		puts("");
	}
}

int work5()
{
	int i, j;
	
	for(i=1; i<=5; i++)
	{
		for(j=i; j<=5; j++ )
			printf("%d",i);
		puts("");
	}
}


int work6()
{
	int i, j;
	
	for(i=1; i<=5; i++)
	{
		for(j=1; j<i; j++)
			printf(" ");
		for(j=i; j<=5; j++ )
			printf("%d",i);
		puts("");
	}
}

int work7()
{
	int i,j;
	
	for (i=1; i<= 5; i++)
	{
		for (j=1; j<=i; j++)
			printf("*");
		puts("");
	}
}

int work8()
{
	int i,j;
	
	for(i=5; i>=1; i--)
	{
		for(j=1; j<=i; j++)
			printf("*");
		puts("");
	}
}

int work9()
{
	int x,y;
	
	for(x=5; x>=1; x--)
	{
		for(y=5; y>x; y--)
			printf(" ");
		for(y=1; y<=x; y++)
			printf("*");
		puts("");
	}
}

int work10()
{
	int x,y;
	
	for (x=1; x<=5; x++)
	{
		for(y=5; y>x; y--)
			printf(" ");
		for(y=1; y<=x; y++)
			printf("*");
		puts("");
	}
}
