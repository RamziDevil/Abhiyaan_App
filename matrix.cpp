#include <bits/stdc++.h>

using namespace std;
int main()
{
    //inputting values
    int m,n,k;
    cin>>m>>n;
    cin>>k;
    int mat[m][n];
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            cin>>mat[i][j];
        }
    }
    int isin=0,i,j;
    for(i=0;i<m;++i){
        for(j=0;j<n;++j){
            if(mat[i][j]==k){
                isin=1;
                goto end;   //breaking loop if k found
            }
            else if(k<mat[i][j])goto end;  //braking loop if matrix values become greater than k
        }                                  
    }
    end:
    if(isin==0){
        cout<<"False"<<endl;
    }
    else{
        cout<<"True"<<endl;
        cout<<i<<" "<<j<<endl;
    }
    return 0;
}

