#include<iostream>
#include<climits>
using namespace std;
int main (){
    int cp;
    cout<<"enter the cost od the product: ";
    cin>>cp;
    int sp;
    cout<<"enter the price of the product: ";
    cin>>sp;
    if(sp>cp) cout<<"profit";
    if(sp<cp) cout<<"loss";
    if(sp==cp) cout<<" no loss,  no profit ";
   




    
}