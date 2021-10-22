#include <iostream>
#include <algorithm>
using namespace std;

double median(int arr[], int size){
   sort(arr, arr+size);
   if (size % 2 != 0)
      return (double)arr[size/2];
   return (double)(arr[(size-1)/2] + arr[size/2])/2.0;
}

void mergeArrays(int arr1[], int arr2[], int n1,
                             int n2, int arr3[])
{
    int i = 0, j = 0, k = 0;
 
    // Traverse both array
    while (i<n1 && j <n2)
    {
        // Check if current element of first
        // array is smaller than current element
        // of second array. If yes, store first
        // array element and increment first array
        // index. Otherwise do same with second array
        if (arr1[i] < arr2[j])
            arr3[k++] = arr1[i++];
        else
            arr3[k++] = arr2[j++];
    }
 
    // Store remaining elements of first array
    while (i < n1)
        arr3[k++] = arr1[i++];
 
    // Store remaining elements of second array
    while (j < n2)
        arr3[k++] = arr2[j++];


    int size = sizeof(arr3);

   //cout << median(arr3, size);
   cout << size;
}
 
// Driver code
int main()
{
    int arrOne[10], arrTwo[10], arrMerge[20];
    int sizeOne, sizeTwo, i;

    cout << "Enter the Size for First Array: ";
    cin >> sizeOne;

    cout << "Enter " << sizeOne << " Elements for First Array: ";
    for (i = 0; i < sizeOne; i++)
    {
        cin >> arrOne[i];;
    }
    int n1 = sizeof(arrOne) / sizeof(arrOne[0]);

    cout << "\nEnter the Size for Second Array: ";
    cin >> sizeTwo;

    cout << "Enter " << sizeTwo << " Elements for Second Array: ";
    for (i = 0; i < sizeTwo; i++)
    {
        cin >> arrTwo[i];
    }
    int n2 = sizeof(arrTwo) / sizeof(arrTwo[0]);


    int arrThree[n1+n2];
    mergeArrays(arrOne, arrTwo, n1, n2, arrThree);
 
    // cout << "Array after merging" <<endl;
    // for (int i=0; i < n1+n2; i++)
    //     cout << arrThree[i] << " ";
 
    return 0;
}