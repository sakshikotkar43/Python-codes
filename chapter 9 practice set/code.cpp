#include <bits/stdc++.h>
using namespace std;

int main(){
    long double N;
    cin >> N;
    if(ceil(N)==floor(N)){
        cout << "int " << N << endl;
    }
    else{
        cout << "float " << floor(N)<< " " <<N-floor(N)<< endl;
        }
return 0;

}