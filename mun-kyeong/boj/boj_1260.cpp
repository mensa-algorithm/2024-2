#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

int node, edge, start;
queue<int> queues;
stack<int> stacks;
vector<int> result;
vector<int> visited;
vector<vector<int> > graph;

//BFS
vector<int> BFS(int start){
    result.push_back( queues.front() );
    visited.push_back( queues.front() );
    queues.pop();
    for(int i=0; i<graph[start].size(); i++){
       if(find(visited.begin(), visited.end(), graph[start][i]) == visited.end()){
           queues.push(graph[start][i]);
           visited.push_back(graph[start][i]);
       }
    }
    if(queues.empty()) return result;
    return BFS(queues.front()); 
}

vector<int> DFS(int start){
    for(int i=0; i<graph[start].size(); i++){
        if(find(visited.begin(), visited.end(), graph[start][i]) == visited.end()){
            visited.push_back(graph[start][i]);
            result.push_back(graph[start][i]);
            stacks.push(graph[start][i]);
            return DFS(graph[start][i]);
        }
    }
    stacks.pop();
    if(stacks.empty()) return result;
    return DFS(stacks.top());
}

int main(){
    cin >> node >> edge >> start;
    for(int i = 0; i < node+1; i++){
        vector<int> initVec;
        graph.push_back(initVec);
    }
    for(int i = 0; i < edge; i++){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for(int i= 0; i<node+1; i++){
        sort(graph[i].begin(), graph[i].end());
    }

    queues.push(start);
    stacks.push(start);
    result.push_back(start);
    visited.push_back(start);
    vector<int> dfs = DFS(start);
    for(int i : dfs) cout<<i<<" ";
    cout<<endl;
    visited.clear();
    result.clear();
    vector<int> bfs = BFS(start);
    for(int i : bfs) cout<<i<<" ";
} 
