#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <windows.h>
#include <string>
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>   
//#include <windows.h> // contain a delay
using namespace std;
//enum type {empty, electric, handicapped};
int main()
{
	int floor0[10] = { 0 }, floor1[10] = { 0 }, floor2[10] = { 0 }, floor3[10] = { 0 }, floor4[10] = { 0 }, floor5[10] = { 0 }, floor6[10] = { 0 }, floor7[10] = { 0 };
	//int seconds = 0;
	//int minute = 0;
	//int hour = 0;
	//int day = 0;
	//int month = 0;
	//int year = 0;
	//int counter = 0;
	bool flag = true;
	int chance;
	ifstream level0, level1, level2, level3, level4, level5, level6, level7;
	ofstream output, output1, output2, output3, output4, output5, output6, output7;//send the data to outfile
	while (flag)
	{
		output.open("f0.txt");
		output1.open("f1.txt");
		output2.open("f2.txt");
		output3.open("f3.txt");
		output4.open("f4.txt");
		output5.open("f5.txt");
		output6.open("f6.txt");
		output7.open("f7.txt");
		for (int i = 0; i < 10; i++)
		{
			floor0[i] = rand() % 3 + 0;
			if (floor0[i] == 0)
			{
				chance = rand() % 1 + 0;
				if (chance == 0)
				{
					floor0[i] = rand() % 1 + 3;
				}
			}
			for (int i = 0; i < 10; i++)
			{
				output << floor0[i] << " ";
			}
			for (int i = 0; i < 10; i++)
			{
				floor1[i] = rand() % 3 + 0;
				if (floor1[i] == 0)
				{
					chance = rand() % 1 + 0;
					if (chance == 0)
					{
						floor1[i] = rand() % 1 + 3;
					}
				}
				for (int i = 0; i < 10; i++)
				{
					output1 << floor1[i] << " ";

				}
				for (int i = 0; i < 10; i++)
				{
					floor2[i] = rand() % 3 + 0;
					if (floor2[i] == 0)
					{
						chance = rand() % 1 + 0;
						if (chance == 0)
						{
							floor2[i] = rand() % 1 + 3;
						}
					}
				}
				for (int i = 0; i < 10; i++)
				{
					output2 << floor2[i] << " ";
				}
				for (int i = 0; i < 10; i++)
				{
					floor3[i] = rand() % 3 + 0;
					if (floor3[i] == 0)
					{
						chance = rand() % 1 + 0;
						if (chance == 0)
						{
							floor3[i] = rand() % 1 + 3;
						}
					}
				}
				for (int i = 0; i < 10; i++)
				{
					output3 << floor3[i] << " ";
				}

				for (int i = 0; i < 10; i++)
				{
					if (floor4[i] == 0)
					{
						chance = rand() % 1 + 0;
						if (chance == 0)
						{
							floor4[i] = rand() % 1 + 3;
						}
					}
				}
				for (int i = 0; i < 10; i++)
				{
					output4 << floor4[i] << " ";
				}
				for (int i = 0; i < 10; i++)
				{
					floor5[i] = rand() % 3 + 0;
					if (floor5[i] == 0)
					{
						chance = rand() % 1 + 0;
						if (chance == 0)
						{
							floor5[i] = rand() % 1 + 3;
						}
					}
				}
				for (int i = 0; i < 10; i++)
				{
					output5 << floor5[i] << " ";
				}
				for (int i = 0; i < 10; i++)
				{
					floor6[i] = rand() % 3 + 0;
					if (floor6[i] == 0)
					{
						floor6[i] = rand() % 4;
					}
				}
				for (int i = 0; i < 10; i++)
				{
					output6 << floor6[i] << " ";
					cout << floor6[i];
				}
				for (int i = 0; i < 10; i++)
				{
					floor7[i] = rand() % 3 + 0;
					if (floor7[i] == 0)
					{
						chance = rand() % 1 + 0;
						if (chance == 0)
						{
							floor7[i] = rand() % 1 + 3;
						}
					}
				}
				for (int i = 0; i < 10; i++)
				{
					output7 << floor7[i] << " ";
				}
				cout << chance<<" ";
				output << endl;
				output1 << endl;
				output2 << endl;
				output3 << endl;
				output4 << endl;
				output5 << endl;
				output6 << endl;
				output7 << endl;
				output.close();
				output1.close();
				output2.close();
				output3.close();
				output4.close();
				output5.close();
				output6.close();
				output7.close();

			}// whileloop ends
		}
	}

}
