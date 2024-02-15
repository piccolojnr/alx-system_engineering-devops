#include <iostream>
#include <vector>

using namespace std;
void print_arr(vector<int> arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i];
        if (i < arr.size() - 1)
            cout << ", ";
    }
    cout << endl;
}
vector<int> quick_sort(vector<int> array)
{
    cout << "quick sort: ";
    print_arr(array);

    const int size = array.size();
    if (size <= 1)
        return array;
    const int pivot = array[0];

    vector<int> left;
    vector<int> right;
    vector<int> middle;

    for (int i = 0; i < size; i++)
    {
        if (array[i] < pivot)
            left.push_back(array[i]);
        else if ((array[i]) > pivot)
            right.push_back(array[i]);
        else
            middle.push_back(array[i]);
    }
    cout << "\tleft: ";
    print_arr(left);
    cout << "\tmiddle: ";
    print_arr(middle);
    cout << "\tright: ";
    print_arr(right);

    left = quick_sort(left);
    right = quick_sort(right);
    left.insert(left.end(), middle.begin(), middle.end());
    left.insert(left.end(), right.begin(), right.end());
    return left;
}

vector<int> insertion_sort(vector<int> array)
{
    cout << "insertion sort: ";
    print_arr(array);

    int size = array.size();

    for (int i = 1; i < size; i++)
    {
        int curr = array[i];
        cout << "sorting position: " << i << " = [" << curr << "]" << endl;
        print_arr(array);
        int k = i;
        for (int j = i - 1; j >= 0; j--)
        {

            if (curr < array[j])
            {
                array[k] = array[j];
                array[j] = curr;
                k--;
            }
            else
                break;
            cout << "\t";
            print_arr(array);
        }
        cout << endl;
    }
    return array;
}

vector<int> bubble_sort(vector<int> array)
{
    cout << "bubble sort: ";
    print_arr(array);

    int size = array.size();

    for (int j = size - 1; j > 0; j--)
    {
        for (int i = 0; i < j; i++)
        {
            if (array[i] > array[i + 1])
            {
                int tmp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = tmp;
            }
            cout << "\t";
            print_arr(array);
        }
    }
    return array;
}

vector<int> selection_sort(vector<int> array)
{
    cout << "selection sort: ";
    print_arr(array);

    int size = array.size();
    for (int i = 0; i < size; i++)
    {
        int k = i;
        for (int j = i + 1; j < size; j++)
        {
            if (array[k] > array[j])
                k = j;
        }
        int tmp = array[i];
        array[i] = array[k];
        array[k] = tmp;
        cout << "\t";
        print_arr(array);
    }
    return array;
}

vector<int> merge_arr(vector<int> arr1, vector<int> arr2)
{
    int n1 = arr1.size(), n2 = arr2.size();
    int i = 0, j = 0;
    vector<int> arr;
    while (i < n1 && j < n2)
    {
        if (arr1[i] <= arr2[j])
        {
            arr.push_back(arr1[i]);
            i++;
        }
        else
        {
            arr.push_back(arr2[j]);
            j++;
        }
    }
    while (i < n1)
    {
        arr.push_back(arr1[i]);
        i++;
    }

    while (j < n2)
    {
        arr.push_back(arr2[j]);
        j++;
    }

    return arr;
}

vector<int> merge_sort(vector<int> array)
{
    if (array.size() < 2)
        return array;

    cout << "selection sort: ";
    print_arr(array);

    size_t const half_size = array.size() / 2;
    vector<int> left(array.begin(), array.begin() + half_size);
    vector<int> right(array.begin() + half_size, array.end());

    left = merge_sort(left);
    right = merge_sort(right);

    vector<int> res = merge_arr(left, right);
    return res;
}
void insertionSort(int arr[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
int main()
{
    int arr[] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};
    int N = sizeof(arr) / sizeof(arr[0]);
    insertionSort(arr, N);
    for (int i = 0; i < N; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}
// int main()
// {
//     vector<int> array = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};
//     cout << "unsorted array" << endl;
//     print_arr(array);
//     cout << endl;
//     vector<int> sorted_array = merge_sort(array);
//     cout << endl;
//     cout << "sorted array" << endl;
//     print_arr(sorted_array);
//     cout << endl;
//     return 0;
// }
