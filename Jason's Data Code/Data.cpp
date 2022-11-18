#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <unistd.h>
//#include <windows.h> // contain a delay
using namespace std;
//enum type {empty, electric, handicapped};

int main()
{
	int floor0[10], floor1[10], floor2[10], floor3[10], floor4[10], floor5[10], floor6[10], floor7[10];
	//int seconds = 0;
	//int minute = 0;
	//int hour = 0;
	//int day = 0;
	//int month = 0;
	//int year = 0;
	//int counter = 0;
	bool flag = true;
	ifstream level0, level1, level2, level3, level4, level5, level6, level7;
	ofstream output; //send the data to outfile


	while (flag)
	{	output.open("/home/pi/projects/output.txt");

		level0.open("/home/pi/projects/f0.txt");
		for (int i = 0; i < 10; i++)
			level0 >> floor0[i];
		level0.close();

		level1.open("/home/pi/projects/f1.txt");
		for (int i = 0; i < 10; i++)
			level1 >> floor1[i];
		level1.close();

		level2.open("/home/pi/projects/f2.txt");
		for (int i = 0; i < 10; i++)
			level2 >> floor2[i];
		level2.close();

		level3.open("/home/pi/projects/f3.txt");
		for (int i = 0; i < 10; i++)
			level3 >> floor3[i];
		level3.close();

		level4.open("/home/pi/projects/f4.txt");
		for (int i = 0; i < 10; i++)
			level4 >> floor4[i];
		level4.close();

		level5.open("/home/pi/projects/f5.txt");
		for (int i = 0; i < 10; i++)
			level5 >> floor5[i];
		level5.close();

		level6.open("/home/pi/projects/f6.txt");
		for (int i = 0; i < 10; i++)
			level6 >> floor6[i];
		level6.close();

		level7.open("/home/pi/projects/f7.txt");
		for (int i = 0; i < 10; i++)
			level7 >> floor7[i];
		level7.close();

		for (int i = 0; i < 10; i++)
		{
			string status[10];

			if (floor0[i] == 1)
				status[i] = "general";

			else if (floor0[i] == 2)
				status[i] = "electric";

			else if (floor0[i] == 3)
				status[i] = "handicap";

			if (floor0[i] != 0)
			{
				cout << "basement" << ".........." << "parking spot " << i + 1 << "..........." << status[i] << endl;
				output << "basement" << ".........." << "parking spot " << i + 1 << ".........." << status[i] << endl;
			}
		}
		cout << endl;
		for (int i = 0; i < 10; i++)
		{
			string status[10];

			if (floor1[i] == 1)
				status[i] = "general";

			else if (floor1[i] == 2)
				status[i] = "electric";

			else if (floor1[i] == 3)
				status[i] = "handicap";

			if (floor1[i] != 0)
			{
				cout << "1st floor" << ".........." << "parking spot " << i + 11 << ".........." << status[i] << endl;
				output << "1st floor" << ".........." << "parking spot " << i + 11 << "..........." << status[i] << endl;
			}
		}
		cout << endl;
		for (int i = 0; i < 10; i++)
		{
			string status[10];

			if (floor2[i] == 1)
				status[i] = "general";

			else if (floor2[i] == 2)
				status[i] = "electric";

			else if (floor2[i] == 3)
				status[i] = "handicap";

			if (floor2[i] != 0)
			{
				cout << "2nd floor" << ".........." << "parking spot " << i + 21 << ".........." << status[i] << endl;
				output << "2nd floor" << ".........." << "parking spot " << i + 21 << "..........." << status[i] << endl;
			}
		}
		cout << endl;
		for (int i = 0; i < 10; i++)
		{
			string status[10];

			if (floor3[i] == 1)
				status[i] = "general";

			else if (floor3[i] == 2)
				status[i] = "electric";

			else if (floor3[i] == 3)
				status[i] = "handicap";

			if (floor3[i] != 0)
			{
				cout << "3rd floor" << ".........." << "parking spot " << i + 31 << ".........." << status[i] << endl;
				output << "3rd floor" << ".........." << "parking spot " << i + 31 << "..........." << status[i] << endl;
			}
		}
		cout << endl;
		for (int i = 0; i < 10; i++)
		{
			string status[10];

			if (floor4[i] == 1)
				status[i] = "general";

			else if (floor4[i] == 2)
				status[i] = "electric";

			else if (floor4[i] == 3)
				status[i] = "handicap";

			if (floor4[i] != 0)
			{
				cout << "4th floor" << ".........." << "parking spot " << i + 41 << ".........." << status[i] << endl;
				output << "4th floor" << ".........." << "parking spot " << i + 41 << "..........." << status[i] << endl;
			}
		}
		cout << endl;
		for (int i = 0; i < 10; i++)
		{
			string status[10];

			if (floor5[i] == 1)
				status[i] = "general";

			else if (floor5[i] == 2)
				status[i] = "electric";

			else if (floor5[i] == 3)
				status[i] = "handicap";

			if (floor5[i] != 0)
			{
				cout << "5th floor" << ".........." << "parking spot " << i + 51 << ".........." << status[i] << endl;
				output << "5th floor" << ".........." << "parking spot " << i + 51 << "..........." << status[i] << endl;
			}
		}
		cout << endl;
		for (int i = 0; i < 10; i++)
		{
			string status[10];

			if (floor6[i] == 1)
				status[i] = "general";

			else if (floor6[i] == 2)
				status[i] = "electric";

			else if (floor6[i] == 3)
				status[i] = "handicap";

			if (floor6[i] != 0)
			{
				cout << "6th floor" << ".........." << "parking spot " << i + 51 << ".........." << status[i] << endl;
				output << "6th floor" << ".........." << "parking spot " << i + 51 << "..........." << status[i] << endl;
			}
		}
		cout << endl;
		for (int i = 0; i < 10; i++)
		{
			string status[10];

			if (floor7[i] == 1)
				status[i] = "general";

			else if (floor7[i] == 2)
				status[i] = "electric";

			else if (floor7[i] == 3)
				status[i] = "handicap";

			if (floor7[i] != 0)
			{
				cout << "7th floor" << ".........." << "parking spot " << i + 61 << ".........." << status[i] << endl;
				output << "7th floor" << ".........." << "parking spot " << i + 61 << "..........." << status[i] << endl;;
			}
		}
		//seconds = counter;
		/*cout << "year : month :day :minute: second" << endl; // send to screen
		output << "year : month :day :minute: second" << endl; // send to text file
		cout << year << " : ";
		cout << month << " : ";
		cout << day << " : ";
		cout << minute << " : ";
		cout << seconds << endl;*/
		//counter++;

				

		//Sleep(3000);
		sleep(10);
		//system("cls"); // clear the screen 
		
		output.close();
	}// whileloop ends

}
