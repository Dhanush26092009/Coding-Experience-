#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;

    int left = 1;      
    int right = n;     
 
    for (int i = 1; i <= n; i++) {
        if (i % 2 != 0) {
            
            cout << left << "\n";
            left++;
        } else {
           
            cout << right << "\n";
            right--;
        }
    }
}
