#include<iostream>
using namespace std;
int main (){
    int age;
    cout<<"Enter the age: ";
    cin>>age;
    if (age>=18) cout<<"Eligible to drive: ";
    else if (age<=0) cout<<"Invalid age:";
    else cout<<"Not eligible to drive: ";
}