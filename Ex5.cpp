#include <iostream>
using namespace std;
 
// Function to rearrange the array in given way.
void rearrangeEvenAndOdd(int arr[], int n){
    int j = -1;
 
    // Quick sort method
    for (int i = 0; i < n; i++) {
 
        // If array of element
        // is odd then swap
        if (arr[i] % 2 == 0) {
 
            // increment j by one
            j++;
 
            // swap the element
            swap(arr[i], arr[j]);
        }
    }
}


 
int main() {

    int size;
    int *sip;

    sip = &size;
    
    cout << "enter size of array: ";
    cin >> size;
    
    int data[size]; //declare array of data
    int dat;

    //fill array
    for(int i = 0; i < size; i++){ 
                  cout << "enter data: ";
                  cin >> dat;
                  data[i] = dat;}


    //int arr[] = {12, 34, 45, 9, 8, 90, 3};
    int n = sizeof(data) / sizeof(data[0]);
 
    rearrangeEvenAndOdd(data, n);
 
    for (int i = 0; i < n; i++)
        cout << data[i] << " ";
}