#include <iostream>
#include <algorithm>
using namespace std;

//calculate median
double median(int arr[], int size)
{
    sort(arr, arr + size);
    if (size % 2 != 0)
        return (double)arr[size / 2];
    return (double)(arr[(size - 1) / 2] + arr[size / 2]) / 2.0;
}

int main()
{
    int arrOne[10], arrTwo[10], arrMerge[20];
    int sizeOne, sizeTwo, i, k;

    cout << "Enter the Size for First Array: ";
    cin >> sizeOne;

    cout << "Enter " << sizeOne << " Elements for First Array: ";
    for (i = 0; i < sizeOne; i++)
    {
        cin >> arrOne[i];
        arrMerge[i] = arrOne[i];
    }

    k = i;

    cout << "\nEnter the Size for Second Array: ";
    cin >> sizeTwo;

    cout << "Enter " << sizeTwo << " Elements for Second Array: ";
    for (i = 0; i < sizeTwo; i++)
    {
        cin >> arrTwo[i];
        arrMerge[k] = arrTwo[i];
        k++;
    }

    int n = *(&arrMerge + 1) - arrMerge;

    cout << n;

    //int arr[] = {3, 5, 2, 1, 7, 8};
    int size = sizeof(arrMerge) / sizeof(arrMerge[0]);
    cout << "Median is : " << median(arrMerge, n) << endl;
    return 0;
}