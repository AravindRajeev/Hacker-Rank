/*
 *
 *
 *  Created on: Aug 27, 2018
 *  Author: Aravind.R
 */
/*
 * Program:Hacker Rank/Variable Sized Array
 *
 */
#include<iostream>
#include<vector>

using namespace std;
int main()
{
	vector <vector <int> >arr1;
	vector <int> arr2;
	vector <int> result;
	vector <int> temp;
	int n,q,size;
	int num,iindex,jindex;
	cin>>n;
	cin>>q;
	for(int i=0;i<n;i++)
	{
		cin>>size;
		arr2.clear();
		for(int j=0;j<size;j++)
		{
			cin>>num;
			arr2.push_back(num);

		}
		arr1.push_back(arr2);
	}

	for(int k=0;k<q;k++)
	{
		cin>>iindex;
		cin>>jindex;
		temp=arr1.at(iindex);
		result.push_back(temp.at(jindex));
	}


	for(int i=0;i<result.size();i++)
	{
		cout<<result.at(i)<<endl;
	}


}
