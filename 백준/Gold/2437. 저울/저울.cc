#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> weights(n);
    for (int i = 0; i < n; ++i) {
        cin >> weights[i];
    }

    sort(weights.begin(), weights.end());

    int minTarget = 0, maxTarget = 0;

    for (int weight : weights) {
        int newMin = minTarget + weight;
        int newMax = maxTarget + weight;

        if (newMin > maxTarget + 1) {
            break;
        } else {
            maxTarget = newMax;
        }
    }

    cout << maxTarget + 1 << endl;
    
    return 0;
}
