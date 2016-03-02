#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
	unsigned long long int N[1501];
	N[1]=1;
	printf("hello");
	int p2=1,p3=1,p5=1;
	for (int n=2; n<=1500; n++){
		while (N[p2]*2 <= N[n-1]) p2++;
		while (N[p3]*3 <= N[n-1]) p3++;
		while (N[p5]*5 <= N[n-1]) p5++;
		N[n] = min (N[p2]*2, min (N[p3]*3, N[p5]*5));
	}
	printf("The 1500'th ugly number is %llu.\n",N[1500]);
}
