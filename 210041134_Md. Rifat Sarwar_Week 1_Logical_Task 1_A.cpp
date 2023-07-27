#include<bits/stdc++.h>

using namespace std;


int dfs(int p);
bool result();


int arr[][2] = {{0,1},{1,2},{2,0},{3,4},{4,5},{5,6},{6,3}};
int n = sizeof(arr)/sizeof(arr[0]);
map<int, bool> visited;
map<int, list<int> > adjlist;

int main()
{


    for(int i=0; i<n; i++)
    {
        adjlist[arr[i][0]].push_back(arr[i][1]);
        adjlist[arr[i][1]].push_back(arr[i][0]);
    }



    map<int, list<int>>::iterator it = adjlist.begin();

    /*

    while (it != adjlist.end())
    {
        std::cout << "Key: " << it->first;

        cout << "  value: ";

        for(auto v: it->second)
        {
            cout << v;
        }

        cout << "\n";
        ++it;
    }

    */

    //cout << "\n\n";

    dfs(0);

    result();


}

int dfs(int p)
{

	visited[p] = true;

	/*

	for(int j=0;j<adjlist.size(); j++)
    {
        cout << visited[j] << " ";
    }
    cout << "\n";

    cout << p << " " << endl;

    */


	list<int>::iterator i;
	for (i = adjlist[p].begin(); i != adjlist[p].end(); ++i)
    {
        //cout << *i << endl;
        if (!visited[*i])
        {
            dfs(*i);
        }

    }

}

bool result()
{
    for(int i=0; i<adjlist.size(); i++){
        if (visited[i] != 1){
            cout << "false";
            return false;
        }
    }
    cout << "true";
    return true;
}
