#include <iostream>
using namespace std;

typedef struct hash_slot
{
    int value;
    hash_slot *next = nullptr;
} hash_slot;

int hash_function(int key)
{
    return key % 9;
}

void hash_table_add(hash_slot *table, int key, int value)
{
    int index = hash_function(key);
    hash_slot *new_slot = new hash_slot;
    new_slot->value = value;
    new_slot->next = nullptr;

    hash_slot *curr = &table[index];

    if (curr == nullptr)
    {
        table[index] = *new_slot;
    }
    else
    {
        while (curr->next != nullptr)
        {
            curr = curr->next;
        }
        curr->next = new_slot;
    }
}

void hash_table_search(hash_slot *table, int key)
{
    int index = hash_function(key);

    const hash_slot *curr = &table[index];

    for (int i = 0; curr != nullptr; i++, curr = curr->next)
    {
        if (key == curr->value)
        {
            cout << "value found at index: " << index << " position: " << i << endl;
            return;
        }
    }
    cout << "value not found\n";
}

void print_hash_table(const hash_slot *table, int size)
{
    for (int i = 0; i < size; i++)
    {
        const hash_slot *curr = &table[i];
        // curr = curr->next; // Skip the dummy head node
        cout << "Index " << i << ": ";

        while (curr != nullptr)
        {
            cout << curr->value << " ";
            curr = curr->next;
        }

        cout << endl;
    }
}

int main()
{
    hash_slot hash_table[9];

    int keys[] = {17, 9, 34, 56, 11, 71, 86, 86, 55, 22, 10, 4, 39, 49, 52, 82, 13, 40, 31, 35, 28, 44};

    for (int k : keys)
    {
        hash_table_add(hash_table, k, k);
    }

    print_hash_table(hash_table, 9);
    while (true)
    {
        int value;
        cout << "Enter a value you wish to find or enter -1 to quit: ";
        cin >> value;

        if (value == -1)
            break;
        else
            hash_table_search(hash_table, value);
    }
    return 0;
}