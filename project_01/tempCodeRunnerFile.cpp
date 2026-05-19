#include <bits/stdc++.h>
using namespace std;

int main(){
    int A, B, C;
cin >> A >> B >> C;
int x = A;
int y = B;
int z = C;

if(A > B){
    swap(A, B);
}

if(B>C){
    swap(B, C);
    if(A>C){
        swap(A, C);
    }
}

cout << A << endl;
cout << B << endl;
cout << C << endl;
cout << endl;
 
cout << x << endl;
cout << y << endl;
cout << z << endl;
return 0;

}