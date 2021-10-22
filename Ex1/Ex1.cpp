#include <iostream>
using namespace std;

void multiplyAdd (int num1, int num2) {
    int addition = num1 + num2;
    int multiplication = num1 * num2;

    cout << "Added: ";
    cout << addition << endl;

    cout << "Multiplied: ";
    cout << multiplication << endl;

}

int main()
{

    int num1;
    int num2;

    int *num1p;
    int *num2p;

    num1p = &num1;
    num2p = &num2;

    cout << "Enter number 1: ";
    cin >> num1;

    cout << "Enter number 2: ";
    cin >> num2;

    multiplyAdd(num1, num2);
}