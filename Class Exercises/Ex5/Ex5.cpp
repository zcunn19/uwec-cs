#include <iostream>
using namespace std;

void rearrangeEvenAndOdd(int arr[], int n)
{
    int j = -1;

    for (int i = 0; i < n; i++)
    {

        // If element is odd then swap
        if (arr[i] % 2 == 0)
        {
            j++;
            // swap the element
            swap(arr[i], arr[j]);
        }
    }
}

int main()
{

    int size, *sip;

    sip = &size;

    cout << "enter size of array: ";
    cin >> size;

    int data[size]; //declare array of data
    int dat;

    //fill array
    for (int i = 0; i < size; i++)
    {
        cout << "enter data: ";
        cin >> dat;
        data[i] = dat;
    }

    int n = *(&data + 1) - data;

    rearrangeEvenAndOdd(data, n);

    for (int i = 0; i < n; i++)
        cout << data[i] << " ";

    return 0;
}