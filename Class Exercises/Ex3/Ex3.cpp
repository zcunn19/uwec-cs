#include <iostream>
using namespace std;

int getOddOccurrence(int arr[], int arr_size)
{
    for (int i = 0; i < arr_size; i++)
    {

        int count = 0;

        for (int j = 0; j < arr_size; j++)
        {
            if (arr[i] == arr[j])
                count++;
        }
        if (count % 2 != 0)
            return arr[i];
    }
    return -1;
}

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

    cout << getOddOccurrence(data, n);
}

int main()
{

    getArray();

    return 0;
}