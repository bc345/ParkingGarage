/*
Name:        Jason Tian
Course ID:   ECET400
Date:        10/06/2022
Description: 
*/

#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	int arr[10];
	double cost[10];

	ifstream park;
	park.open("Floor1.dat");
	for (int i = 0; i < 10; i++)
	{
		park >> arr[i];
	
		if (arr[i] = 0)
			cost[i] = 1;
		else if (arr[i] = 1)
			cost[i] = 2;
		else
			cost[i] = 0;
	}

	park.close();

	
	for (int i = 0; i < 10; i++){
		if (cost[i]) = 1
			cout << "empty";

	}
}

