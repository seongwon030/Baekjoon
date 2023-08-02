#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;

    vector <long long> d(101, -1);
    d[1] = d[2] = d[3] = 1;
    d[4] = d[5] = 2;

    for (int t = 0; t < T; ++t) {
        int n;
        cin >> n;

        for (int i = 6; i <= n; ++i) {
            if (i <= 8) {
                d[i] = d[i - 1] + 1;
            }
            else if (i <= 10) {
                d[i] = d[i - 1] + 2;
            }
            else {
                d[i] = d[i - 1] + d[i - 5];
            }
        }

        cout << d[n] << endl;
    }

    return 0;
}