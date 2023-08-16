#include <iostream>

using namespace std;

int main(void) {
    int a, b;
    int k = 0;
    int re = 0;
    for (int i = 0; i < 10; i++) {
        cin >> a >> b;
        re += (-a + b);
        if (re > k) {
            k=re;
        }
        else {
            continue;
        }
    }
    cout << k;
}