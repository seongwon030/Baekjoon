
#include<iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	string k;

	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> k;
		int result = 0;
		int cnt = 0;
		for (int i = 0; i < k.length(); i++) {
			if (k[i] == 'O') {
				cnt++;
			}
			else {
				cnt = 0;
			}
			result += cnt;
		}

		cout << result << endl;
	}
}