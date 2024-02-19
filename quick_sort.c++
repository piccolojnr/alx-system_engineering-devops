#include <iostream>
#include <vector>
using namespace std;

void printf_arr(int arr[], int low, int high)
{
    for (int i = low; i <= high; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}
void print_arr2(vector<int> arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i];
        if (i < arr.size() - 1)
            cout << ", ";
    }
    cout << endl;
}
int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j <= high; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(arr[i], arr[j]);
        }
        
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}
vector<vector<int>> partition2(vector<int> arr)
{
    vector<int> low;
    vector<int> high;
    vector<int> mid;
    int n = arr.size();
    int pivot = arr[n - 1];

    for (int i = 0; i < n; i++)
    {
        if (arr[i] < pivot)
            low.push_back(arr[i]);
        else if (arr[i] > pivot)
            high.push_back(arr[i]);
        else
            mid.push_back(arr[i]);
    }
    return {low, mid, high};
}
vector<int> quickSort2(vector<int> arr)
{
    if (arr.size() < 1)
        return arr;
    vector<vector<int>> pi = partition2(arr);
    quickSort2(pi[0]);
    quickSort2(pi[2]);
    pi[0].insert(pi[0].end(), pi[1].begin(), pi[1].end());
    pi[0].insert(pi[0].end(), pi[2].begin(), pi[2].end());
    return pi[0];
}
// Example usage
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main()
{
    vector<int> arr = {10, 80, 30, 90, 40};
    vector<int> res = quickSort2(arr);
    print_arr2(res);

    // int arr[] = {10, 80, 30, 90, 40};
    // int n = sizeof(arr) / sizeof(arr[0]);
    // quickSort(arr, 0, n - 1);
    // printf_arr(arr, 0, n - 1);
    return 0;
}
