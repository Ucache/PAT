/*************************************************************************
    > File Name: 1033.toFillOrNotToFill.cpp
    > Author: Meng jl
    > Mail:mjl8789@gmail.com 
    > Created Time: Tue 25 Feb 2014 02:21:24 PM CST
 ************************************************************************/

#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;
struct station
{
    float price;
    float dis;
};
vector<station> stations;
struct car
{
    float remain;
    float coverage;
    float cap;
    float per;
    float walked;
    float cost;
    int no;
    bool reached ;
    car(float c=0,float p=0,float w=0,float co=0,int n=0,bool r=true):
        cap(c),per(p),walked(w),cost(co),no(n),reached(r){
        remain = 0;
        coverage = cap*per;
    }
    int minifill(float dis,int pos)
    {
        //printf("%.2f <->",cost);
        //cost += per*stations[no].price;
        //printf("%.2f\n ",cost);
            printf("min pos @%d\n",pos);
        if(remain*per<=(dis-walked))
        {
            cost += (dis-walked-remain*per)/per * stations[no].price;
            printf("remain:%.2f cannot afford\nadd at pos %d at price %.2f \n",remain,no,stations[no].price);
            remain = 0;
        }
        else
        {
            remain -= (dis-walked)/per;
            printf("remain can afford\n");
        }
        walked = dis;
        no = pos;
    };
    int fullfill()
    {
        printf("full fill the car finally\n");
        cost += (cap-remain)*stations[no].price;
        walked = walked + coverage;
    };
    int fullfill(float dis,int pos)
    {
            printf("min pos @%d\n",pos);
        printf("full fill the car ");
        cost += (cap-remain)*stations[no].price;
        remain = cap;
        walked = dis;
        no = pos;
        printf("cap is %.2f\n",remain);
    }
};
int cmp(const station& a,const station& b)
{

    return a.dis < b.dis;
}
int main()
{
    float cap,dis,per;
    int s;
    scanf("%f %f %f %d",&cap,&dis,&per,&s);
    float fullcanrun = cap*per;
    for(int i=0;i<s;i++)
    {
        station tmp;
        scanf("%f %f",&tmp.price,&tmp.dis);
        stations.push_back(tmp);
    }
    station tmp;
    tmp.price=100000;
    tmp.dis = dis;
    stations.push_back(tmp);
    sort(stations.begin(),stations.end(),cmp);
    printf("\ndistance\n");
    for(int i =0;i<stations.size();i++)
        printf("%f %f\n",stations[i].price,stations[i].dis);
    car c;
    c.coverage = fullcanrun;
    c.cap = cap;
    c.per = per;
    for(int i =1;i<stations.size();i++)
    {
        float currentprice = stations[i-1].price;
        if(stations[i-1].price >= stations[i].price)
        {
            c.minifill(stations[i].dis,i);
        }
        else 
        {
            float minprice=1000000,mindis=-1;
            int minpos=-1;
            for(int j =i;j<stations.size();j++)
            {
                if((stations[j].dis-stations[i-1].dis) > c.coverage)
                    break;
                //printf(">>%d %d\n",i,j);
                if(stations[j].price < minprice)
                    minprice=stations[j].price,mindis=stations[j].dis,minpos=j;
            }
            if(mindis != -1)
                if (minprice <= currentprice )
                    c.minifill(mindis,minpos),i=minpos;
                else if (minpos == stations.size()-1)
                    c.minifill(mindis,minpos),i=minpos;
                else
                    c.fullfill(mindis,minpos),i=minpos;
            else
            {
                c.fullfill();
                c.reached = false;
                break;
            }
        }
    }
    if(c.reached) printf("%.2f\n",c.cost);
    else printf("The maximum travel distance = %.2f\n",c.walked);

}
