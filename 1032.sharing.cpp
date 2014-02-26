/*************************************************************************
    > File Name: 1032.sharing.cpp
    > Author: Meng jl
    > Mail:mjl8789@gmail.com 
    > Created Time: Tue 25 Feb 2014 01:51:03 PM CST
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>

using namespace std;
int binary(vector<int> a, vector<int> b)
{
    int sub = a.size() - b.size();
    int common=-1,low=0,high=b.size()-1;
    while(low <= high)
    {
        int mid = (low+high)/2;
        if(a[sub+mid] == b[mid])
            high=mid-1,common=b[mid];
        else
            low=mid+1;
    }
    return common;
}
int main()
{
    int s1,s2,n;
    //cin>>s1>>s2>>n;
    scanf("%d %d %d",&s1,&s2,&n);
    int r[100000];
    memset(r,-1,100000);
    for(int i=0;i<n;i++)
    {
        int s,e;
        char w;
        //cin>>s>>w>>e;
        scanf("%d %c %d",&s,&w,&e);
        r[s] = e;
    }
    vector<int> a,b;
    while(s1 != -1)
        a.push_back(s1),s1=r[s1];
    while(s2 != -1)
        b.push_back(s2),s2=r[s2];
    int common = -1;
    if(a.size()>b.size()) 
        common = binary(a,b);
    else
        common = binary(b,a);
    if(common == -1) printf("-1\n");
    else printf("%.5d\n",common);
}
