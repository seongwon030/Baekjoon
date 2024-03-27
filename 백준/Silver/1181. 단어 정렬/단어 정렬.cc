#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool com(const string &s1, const string &s2)
{
    if (s1.size() == s2.size()) // 크기가 같을 때 사전순
    {
        return s1 < s2;
    }
    return s1.size() < s2.size(); // 크기 다를 때 길이순
}

int main()
{    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    vector<string> result;
    for (int i = 0; i < n; i++)
    {
        string word;
        cin >> word;

        result.push_back(word);
    }
    sort(result.begin(), result.end(), com);
    result.erase(unique(result.begin(), result.end()), result.end()); // 중복문자 제거
    for (int i = 0; i < result.size(); ++i)
    {
        cout << result[i] << endl;
    }
    return 0;
}