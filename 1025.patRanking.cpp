/*************************************************************************
    > File Name: 1025.patRanking.cpp
    > Author: Meng jl
    > Mail:mjl8789@gmail.com 
    > Created Time: Mon 24 Feb 2014 06:55:52 PM CST
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;
struct testee
{
    string id;
    int score,finalrank,location,localrank;
    testee(string i,int s,int l):id(i),score(s),location(l)
    {
        finalrank=-1;
        localrank=-1;
    }
};
int cmp(const testee& a, const testee& b)
{
    if(a.score == b.score)
        return a.id < b.id;
    else
        return a.score > b.score;
}
int main()
{
    int n;
    //scanf("%d",&n);
    cin>>n;
    vector<testee> total;
    vector<vector<testee> > lists;
    for(int i=0;i<n;i++)
    {
        string id;
        int score;
        int localn;
        cin>>localn;
        vector<testee> localtestee;
        for(int j=0;j<localn;j++)
        {
            cin>>id>>score;
            testee t(id,score,i);
            localtestee.push_back(t);
        }
        lists.push_back(localtestee);
    }
    for(int i=0;i<lists.size();i++)
    {
        sort(lists[i].begin(),lists[i].end(),cmp);
        lists[i][0].localrank = 0;
        total.push_back(lists[i][0]);
        for(int j=1;j<lists[i].size();j++)
        {
            if(lists[i][j-1].score != lists[i][j].score)
            {
                lists[i][j].localrank = j;
            }
            else
            {
                lists[i][j].localrank = lists[i][j-1].localrank;
            }
            total.push_back(lists[i][j]);
        }
    }
    sort(total.begin(),total.end(),cmp);
    total[0].finalrank = 0;
    for(int i=1;i<total.size();i++)
    {
        if(total[i-1].score != total[i].score)
        {
            total[i].finalrank = i;
        }
        else
        {
            total[i].finalrank = total[i-1].finalrank;
        }
    }
    cout<<total.size()<<endl;
    for(int i=0;i<total.size();i++)
    {
        cout<<total[i].id<<" "<<total[i].finalrank+1<<" "<<total[i].location+1<<" "<<total[i].localrank+1<<endl;
    }
}
