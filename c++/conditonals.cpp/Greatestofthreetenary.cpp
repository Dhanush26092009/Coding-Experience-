#include<iostream>
using namespace std;
int main () {
    int a=45 , b=27 , c=35;
    int x = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
    cout<<x;

}