#include <iostream>
#include <algorithm>

using namespace std;

double median(int arr[], int size)
{
    sort(arr, arr + size);
    if (size % 2 != 0)
        return (double)arr[size / 2];
    return (double)(arr[(size - 1) / 2] + arr[size / 2]) / 2.0;
}

void mergeArrays()
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

    int size2;
    cout << "enter size of array: ";
    cin >> size2;

    int data2[size2]; //declare 2nd array
    int dat2;

    //fill array 2
    for (int i = 0; i < size2; i++)
    {
        cout << "enter data: ";
        cin >> dat2;
        data2[i] = dat2;
    }

    //copy data from data & data2 to arr
    int m = *(&data + 1) - data;
    int n = *(&data2 + 1) - data2;

    int arr[m + n];
    std::copy(data, data + m, arr);
    std::copy(data2, data2 + n, arr + m);

    //print median
    int arrSize = sizeof(arr) / sizeof(arr[0]);

    //sort array
    sort(arr, arr + arrSize);

    //print new *sorted* array
    cout << endl
         << "Sorted Array: ";
    for (int i = 0; i < m + n; i++)
    {
        std::cout << arr[i] << ' ';
    }

    cout << endl;
    cout << "Median: " << median(arr, arrSize);
}

int main()
{
    mergeArrays();

    return 0;
}