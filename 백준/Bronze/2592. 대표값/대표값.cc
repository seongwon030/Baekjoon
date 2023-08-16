#include <iostream>
using namespace std;

int main(void) {
    int a;
    int m = 0;
    int k[1000] = { 0, };
    int size = 0;

    for (int i = 0; i < 10; i++) {
        cin >> a;
        if (size < a) {
            size = a;
        }
        m += a;
        k[a] += 1;
    }

    int max = 0;
    for (int j=0; j <= size; j++) {
        if (k[j] == 0) {
            continue;
        }
        else {
            if (k[max] < k[j]) {
                max = j;
            }
            else {
                continue;
            }
        }
    }
    cout << m / 10 << endl;
    cout << max;
}