/*
Author: Maisa Ahmad
Course: CSCI-136
Instructor: Genady Maryash
Assignment: Leap, Lab 1C

This program will prompt for an integer representing a year, if it is a leap year, 
the program will print leap year. 
Otherwise, it will print common year.
*/

#include <iostream>
using namespace std;

int main()
{
	cout<<“Enter year: “<<endl;
	cin>>yr;
	int yr=0

    if (year % 4 != 0)
    {
        if (year % 100 != 0)
        {
            if (year % 400 != 0)
                cout <<“Common year”;
            else
                cout << year << “Leap year“;
        }
        else
            cout << year << “Common year“;
    }
    else
        cout << year << “Leap year“;

    return 0;
}