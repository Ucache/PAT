#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    float a, b , c;
    float sum=1;
    while(cin>>a>>b>>c)
    {
        if(a>b&&a>c)
        {
            printf("W ");
            sum*=a;
        }
        else if(b>a&&b>c)
        {
            printf("T ");
            sum*=b;
        }
        else if(c>a&&c>b)
        {
            printf("L ");
            sum*=c;
        }
    }
    printf("%.2f\n",(sum*0.65-1)*2);
}
