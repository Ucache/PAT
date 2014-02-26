/*************************************************************************
    > File Name: 1015.reversiblePrimes.cpp
    > Author: Meng jl
    > Mail:mjl8789@gmail.com 
    > Created Time: Sun 23 Feb 2014 08:59:12 PM CST
 ************************************************************************/

#include<iostream>
#include<cmath>
#include<cstdio>
#include<stack>
using namespace std;
int isprime(int n)
{
    for(int d=2;(d*d)<(n+1);++d)
    {
        if(!(n%d))
            return false;
    }
    if(n==1) return false;
    else
    return true;
}
int trans(int n,int base)
{
    stack<int> result;
    while(n)
    {
        result.push(n%base);
        n/=base;
    }
    int sum = 0;
    int pos = 0;
    while(!result.empty())
    {
        sum += result.top() * pow(base,pos++);
        result.pop();
    }
    return sum;
}
int main()
{
    int n,m;
    while(scanf("%d",&n) )
    {
        if(n<0) return 0;
        scanf("%d",&m);
        //printf("%d %d\n",n,trans(n,m));
        if(isprime(n) && isprime(trans(n,m)))
            printf("Yes\n");
        else
            printf("No\n");
    }
    return 0;
}
