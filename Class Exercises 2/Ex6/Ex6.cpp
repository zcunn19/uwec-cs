#include <iostream>
using namespace std;

void getArray()
{
    int size;
    cout << "enter size of array: ";
    cin >> size;

    int data[size]; //declare array
    int dat;

    //fill array
    for (int i = 0; i < size; i++)
    {
        cout << "enter data: ";
        cin >> dat;
        data[i] = dat;
    }

    int n = *(&data + 1) - data;



}