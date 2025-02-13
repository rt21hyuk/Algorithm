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

    int maxTarget = 0;

    for (int weight : weights) {
        if (weight > maxTarget + 1) {
            break;
        }
        maxTarget += weight;
    }

    cout << maxTarget + 1 << endl;
    return 0;
}
