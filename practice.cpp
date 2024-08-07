#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool PalinArray(int arr[] ,int n )
{
    


    for (int i = 0; i < n; i++)
    {

        int num = arr[i];
        int result = 0;
        int original = num;

        while (num != 0)
        {
            int digit = num % 10;
            result = result * 10 + digit;
            num /= 10;
        }
        if (result != original)
        {
            return false;
        }
       

    }
     return true;
   
}


int main() {
    int arr[] = {121, 131, 141};
    int size = sizeof(arr) / sizeof(arr[0]);

    bool result = PalinArray(arr, size);
    if (result) {
        cout << "All numbers in the array are palindromes." << endl;
    } else {
        cout << "Not all numbers in the array are palindromes." << endl;
    }

    return 0;
}