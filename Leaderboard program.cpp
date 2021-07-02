#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define all(x)     		(x).begin(),(x).end()
#define ub    			upper_bound
#define lb 				lower_bound
#define ins				insert
#define int 			long long
#define endl			'\n'
#define ff              first
#define ss              second
#define ull				unsigned long long
#define pb              push_back
#define mp              make_pair
#define pii             pair<int,int>
#define vi              vector<int>
#define si 				set<int>
#define usi 			unordered_set<int>		
#define mii             map<int,int>
#define umii			unordered_map<int ,int>
#define pqb             priority_queue<int>
#define pqs             priority_queue<int,vi,greater<int> >
#define rep(i,a,n)		for(int i=a;i<n;++i)
#define repd(i,a,n)		for(int i=a;i>n;--i)
#define setbits(x)      __builtin_popcountll(x)
#define zerobits(x)      __builtin_ctzll(x)
#define Mod             1000000007
#define inf             1e18
#define ps(x,y)         fixed<<setprecision(y)<<x
#define mk(arr,n,type)  type *arr=new type[n];
#define w(x)            int x; cin>>x; while(x--)
#define deb(x)			cout<<#x <<"="<<x<<endl;
#define deb2(x,y)		cout<<#x<<"="<<x<<"  "<<#y<<"="<<y<<endl;
mt19937                 rng(chrono::steady_clock::now().time_since_epoch().count());

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
int Pow(int a,int b){int res=1;while(b>0){if(b&1)res*=a;a*=a;b/=2;}return res;}
int MPow(int a,int  b){int res=1;while(b>0){if(b&1)res=(res*a)%Mod;a=(a*a)%Mod;b/=2;}return res%Mod;}
int log(int x){return 64-__builtin_clzll(x)-1;}

void c_p_p()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
}
struct Node
{
	int m,pts,w,run_scored=0,runs_conceded=0;
	double rr=0.0,over_bat=0,over_ball=0;
	string name;

	
};
bool cmp(Node A,Node B)
{
	if(A.pts!=B.pts)
		return A.pts>B.pts;
	return A.rr>B.rr;
}
const int Max=1e5+1;
const int total=8;
string t1,t2;
double s1,s2,o1,o2;
Node Team[total];
void Standing()
{
	//deb2(t1,t2);
	int f,s;
	rep(i,0,total)
	{
		if(Team[i].name==t1)f=i+1;
		if(Team[i].name==t2)s=i+1;
		
	}
	cout<<s<<endl;
	
}
void Match()
{

	rep(i,0,total)
	{
		if(Team[i].name==t1)
		{
			Team[i].m+=1;
			Team[i].pts+=2;
			Team[i].w+=1;
			Team[i].run_scored+=s1;
			Team[i].runs_conceded+=s2;
			Team[i].over_ball+=o2;
			Team[i].over_bat+=o1;
			double val=(Team[i].run_scored/Team[i].over_bat)-(Team[i].runs_conceded/Team[i].over_ball);
			Team[i].rr=val;
		}
		if(Team[i].name==t2)
		{
			Team[i].m+=1;
			Team[i].run_scored+=s2;
			Team[i].runs_conceded+=s1;
			Team[i].over_ball+=o1;
			Team[i].over_bat+=o2;
			double val=(Team[i].run_scored/Team[i].over_bat)-(Team[i].runs_conceded/Team[i].over_ball);
			Team[i].rr=val;

		}
	}


}
void Leaderboard()
{
	sort(Team,Team+total,cmp);
	/*cout<<"Pos.  Team    Match   Win   Pts    Runrate"<<endl;
	rep(i,0,8)
	{
		cout<<i+1<<"      ";
		cout<<Team[i].name;
		if((Team[i].name).size()==2)cout<<"  ";
		if((Team[i].name).size()==3)cout<<" ";
		cout<<"    ";
		cout<<Team[i].m<<"      "<<Team[i].w<<"      "<<Team[i].pts<<"      "<<ps(Team[i].rr,3)<<endl;

	}*/
}


int32_t main()
{
	c_p_p();
	string Teams[total]={"CSK","RR","DC","SRH","RCB","KKR","KXIP","MI"};
	sort(Teams,Teams+total);
	rep(i,0,total)Team[i].name=Teams[i];
	//rep(i,0,8)cout<<Team[i].name<<" ";
	int cnt=1;
	w(t)
	{
		cin>>t1>>s1>>o1>>t2>>s2>>o2;
		//cout<<"Match No- "<<cnt++<<" "<<endl;
		//cout<<t1<<" VS "<<t2<<endl;
		Standing();
		Match();
		Leaderboard();

	}
	return 0;
}
	