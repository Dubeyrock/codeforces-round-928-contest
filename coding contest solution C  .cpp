#include<bits/stdc++.h>
using namespace std;

void solve(){
  
  return;
}
int main(){
    int t;
    cin>>t;
    int d[200001];
  d[1]=1; 
    for(int i=2;i<=200001;i++){ 
        int k=i,sum=0; 
        while(k>0){ 
            sum+=k%10; 
            k/=10; 
        } 
        d[i]=d[i-1]+sum; 
    }
    while(t--){
      int n;
      cin>>n;
      cout<<d[n]<<"\n";
  }
  return 0;
}
