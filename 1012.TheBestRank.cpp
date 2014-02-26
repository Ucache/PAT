#include <cstdio>
#include <vector>
#include <algorithm>
struct stu
{
    int id;
    int c,m,e;
    float a;
    int rank=-1;
    int rankno = -1;
    stu(int idd,int cp,int ma,int en,float av):id(idd),c(cp),m(ma),e(en),a(av){

    }
};
int cmp0(const stu a, const stu b, int j)
{
    return a->
}
int main()
{
    int n,q;
    scanf("%d %d",&n,&q);
    vector<stu> s;
    for(int i=0;i<n;i++)
    {
        int id,c,m,e,a;
        scanf("%d %d %d %d",&id,&c,&m,&e);
        stu tmp(id,c,m,e,(c+m+e)/3.0);
        s.push_back(tmp);
    }
    int rank[1000000];
    int rankno[1000000];
    memset(rankno,-1,1000000);
    memset(rank,3000,1000000);
    for(int j=0;j<4;j++)
    {
        sort(v.begin(),v.end(),cmp(j));
        for(int i=0;i<v.size();i++)
        {
           if(rank[v[id]] < i) rank[v[id]] = i,rankno[v[id]] = j; 
        }
    }
    for(int i=0;i<q;i++)
    {
        int query;
        scanf("%d",&query);
        if(rank[query] != 3000) printf("%d %d\n",rank[query],rankno[query]);
        else printf("N/A\n");
    }
}
