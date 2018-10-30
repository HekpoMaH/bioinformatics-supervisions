#include<bits/stdc++.h>
using namespace std;
int dp[100][100];
// blosum 50 taken from
// https://www.ncbi.nlm.nih.gov/IEB/ToolBox/C_DOC/lxr/source/data/BLOSUM50/
map<char,map<char, int> >BLOSUM50;
int main() {
    // I should have chosen Python...
    string seq1="PAWHEAE", seq2="HEAGAWGHEE";
    // cin>>seq1>>seq2; // uncomment if you want any input
    int n=seq1.size(), m=seq2.size();
    for (int i=0; i<=n; i++) {
        dp[i][0] = -i*8;
    }
    for (int j=0; j<=m; j++) {
        dp[0][j] = -j*8;
    }
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            cout<< BLOSUM50[seq1[i-1]-'A'][seq2[j-1]-'A'] << dp[i-1][j]-8<<dp[i][j-1]-8<<endl;
            dp[i][j] = max(
                    dp[i-1][j-1] + BLOSUM50[seq1[i-1]-'A'][seq2[j-1]-'A'],
                    max(dp[i-1][j], dp[i][j-1]) - 8);
        }
    }
    for (int i=0; i<=n; i++) {
        for (int j=0; j<=m; j++) {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
    cout << dp[n][m] << endl;
}
