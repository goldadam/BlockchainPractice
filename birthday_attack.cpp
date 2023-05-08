#include <iostream>
#include <iomanip>
#include <cmath>
#include <bits/stdc++.h>
#define div 365
using namespace std;

int main() {

    int n;
    cout << "Enter the number of people in the room: ";
    cin >> n;

    double p = 1;
    for (int i = 1; i < n; i++) {
        p *= (div - i) / div;
    }

    double probability = (1 - p) * 100;
    cout << "The probability of at least two people having the same birthday is: " << fixed << setprecision(6) << probability << "%" << endl;

    return 0;
}

