// C++ program to implement the Quick Sort
// using OMI
#include <bits/stdc++.h>
#include <omp.h>
#include <time.h>
#include <sys/time.h>

using namespace std;

double start_time, end_time; /* start and end times */

double read_timer() {
    static bool initialized = false;
    static struct timeval start;
    struct timeval end;
    if( !initialized )
    {
        gettimeofday( &start, NULL );
        initialized = true;
    }
    gettimeofday( &end, NULL );
    return (end.tv_sec - start.tv_sec) + 1.0e-6 * (end.tv_usec - start.tv_usec);
}


// Function to swap two numbers a and b
void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

// Function to perform the partitioning
// of array arr[]
int partition(int arr[], int start, int end)
{
    // Declaration
    int pivot = arr[end];
    int i = (start - 1);

    // Rearranging the array
    for (int j = start; j <= end - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[end]);

    // Returning the respective index
    return (i + 1);
}

// Function to perform QuickSort Algorithm
// using openmp
void quicksort(int arr[], int start, int end)
{
    // Declaration
    int index;

    if (start < end) {

        // Getting the index of pivot
        // by partitioning
        index = partition(arr, start, end);

// Parallel sections
#pragma omp parallel sections
        {
#pragma omp section
            {
                // Evaluating the left half
                quicksort(arr, start, index - 1);
            }
#pragma omp section
            {
                // Evaluating the right half
                quicksort(arr, index + 1, end);
            }
        }
    }
}

// Driver Code
int main()
{
    // Declaration
    int N;

    // Taking input the number of
    // elements we wants
    cin >> N;

    // Declaration of array
    int arr[N];

    // Taking input that array
    for (int i = 0; i < N; i++) {
        arr[i] = rand() % N;
    }

    // Calling quicksort having parallel
    // code implementation
    start_time = read_timer();
    quicksort(arr, 0, N - 1);
    end_time = read_timer();

    cout << "OMP: Time: " << end_time - start_time << endl;
    return 0;
}
