//Maisa Ahmad
//July 9, 2018
//Prints greeting based on season

#include <iostream>            
using namespace std; 

int main () 
{
    int month;
    cout << "Enter a month: ";
    cin >> month;
 
    if (month < 3 || month > 11) 
        cout << "Happy Winter\n";   
    if (month >= 3 && month < 7)
        cout << "Happy Spring";
    if (month >= 7 && month < 9) 
        cout << "Happy Summer\n";
    else
        cout << "Happy Fall\n";

    
        
    return(0);
}
