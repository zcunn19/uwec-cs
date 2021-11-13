#include <iostream>
using namespace std;

void multiplyAdd()
{
    int num1, num2, *num1p, *num2p;

    cout << "Enter number 1: ";
    cin >> num1;

    num1p = &num1;

    cout << "Enter number 2: ";
    cin >> num2;

    num2p = &num2;

    int addition = *num1p + *num2p;
    int multiplication = *num1p * *num2p;

    cout << "Added: ";
    cout << addition << endl;

    cout << "Multiplied: ";
    cout << multiplication << endl;
}


int main()
{
    multiplyAdd();

    return 0;
}