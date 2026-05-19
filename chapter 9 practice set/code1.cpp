#include <iostream>
using namespace std;

int main() {
    int N, i;
    cin >> N;

    int a[N];
    for (i = 0; i < N; i++) {
        cin >> a[i];
    }

    int pos = 0, neg = 0, even = 0, odd = 0;

    for (i = 0; i < N; i++) {
        if (a[i] > 0)
         pos++;
        if (a[i] < 0) 
        neg++;
        if (a[i] % 2 == 0) 
        even++;
        if (a[i] % 2 != 0)
         odd++;
    }
        cout << "Even: " << even << endl;
        cout << "Odd: " << odd << endl;
       cout << "Positive: " << pos << endl;
       cout << "Negative: " << neg << endl;

    return 0;
}