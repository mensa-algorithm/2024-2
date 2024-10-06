#include <iostream>

using namespace std;

int main(){

string str;
    bool isMinus = false;
    int num=0;
    int answer= 0;
    int minusSum= 0;
    cin>>str;
    for(char c : str){
        if(c == '-') {
            minusSum += num;
            if(!isMinus) answer+=minusSum;
            else answer -= minusSum;
            num = 0;
            minusSum = 0;
            isMinus = true;   
        }
        else if(c == '+') {
            minusSum += num;
            num = 0;
        }
        else {
            num*=10;
            num += c - '0';
            continue;
        }
    }
    minusSum += num;
    if(isMinus) answer -= minusSum;
    else answer += minusSum;
    
    cout<<answer<<endl;
}
