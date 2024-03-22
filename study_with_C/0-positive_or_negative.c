#include <stdlib.h>
#include <time.h>
#include <stdio.h>
/**
 * main - Program starts here
 *
 * Return: prints string; 0 otherwise
 */

int main(void)
{
	int n;

	srand(time(0));
	n = rand() - RAND_MAX / 2;
	if(n > 0)
		printf("%d is positive\n", n);
	else if (n < 0)
		printf("%d is negative\n", n);
	else (n == 0)
		printf("%d is zero\n", n);

	return (0);
}