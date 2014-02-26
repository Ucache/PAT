/*************************************************************************
    > File Name: 1010.radix.cpp
    > Author: Meng jl
    > Mail:mjl8789@gmail.com 
    > Created Time: Mon 24 Feb 2014 12:10:34 AM CST
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<cmath>
using namespace std;
long long str2int(string s,long long radix)
{
    long long sum = 0;
    long long pos = 0;
    for(int i=s.length()-1;i>=0;i--)
    {
        if(s[i] >= '0' && s[i] <= '9')
            sum += (s[i]-'0') * pow(radix,pos);
        else if(s[i] >='a' && s[i] <= 'z')
            sum += (s[i]-'a'+10) * pow(radix,pos);
        pos++;
    }
    return sum;
}
int max(string s)
{
    int maxi = 0;
    int tmp;
    for(int i=0;i<s.length();i++)
    {
        if(s[i] >= '0' && s[i] <= '9')
            tmp = (s[i]-'0');
        else if(s[i] >='a' && s[i] <= 'z')
            tmp = (s[i]-'a'+10);
        if(maxi < tmp)
        {
            maxi = tmp;
        }
    }
    return maxi;
}
int binarySearch(string s,long long low,long long high, long long target)
{
    long long mid = -1;
    long long p;
    while(low <= high)
    {
        mid = (low + high)/2;
        //int flag = cmp(s,mid,target);
        p = str2int(s,mid);
        //printf("%lld %lld\n",mid,p);
        if(p== target)
        {
            return mid;
        }
        else if (p >target)
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return -1;
}
int main()
{
    long long radix;
    int tag;
    string n1,n2;
    cin>>n1>>n2>>tag>>radix;
    if(tag == 2)
    {
        string tmp = n2;
        n2 = n1;
        n1 = tmp;
    }
    long long low,high;
    long long target = str2int(n1,radix);
    long long p = str2int(n2,radix);
    if(p > target)
    {
        low = max(n2) + 1;
        high = radix - 1;
    }
    else if(p < target)
    {
        low = radix + 1;
        high = target ;
    }
    else
    {
        printf("%lld\n",radix);
        return 0;
    }
    //printf("target %lld\n%lld<-->%lld\n",target,low,high);
    if(binarySearch(n2,low,high,target) != -1)
        printf("%lld\n",binarySearch(n2,low,high,target));
    else
        printf("Impossible\n");
    return 0;
}
