// C++ program to implement the Quick Sort
// using POSIX Thread
#include <bits/stdc++.h>
#include <pthread.h>
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

// Structure
struct data_set {
    int start_index;
    int end_index;
    int* data;
};

// Function to perform swap operations
void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

// Partition function for making
// partition in array
int partition(int arr[], int left_index,
              int right_index)
{
    // Declaration and initialization
    // choosing pivot element form which
    // we make partition

    // Here pivot is last element of
    // the array
    int pivot = arr[right_index];
    int i = left_index - 1;

    // Making array as per requirement
    // arranging element smaller than
    // pivot on left side and larger
    // then pivot on right side
    for (int j = left_index;
         j <= right_index - 1; j++) {

        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[right_index]);

    // Returning the partition index
    return i + 1;
}

// Quicksort Function for sorting
// array
void* quick_sort(void* data)
{

    // Retrieving back the data sent
    // from thread
    struct data_set* info = (struct data_set*)data;

    // Declaration of left index
    int left_index, right_index, index;

    // Initialization of left and
    // right index
    left_index = info->start_index;
    right_index = info->end_index;

    // Recursive call of quick_sort
    // function
    if (left_index < right_index) {

        // Declaration of pthread and
        // pthread attribute type object
        pthread_attr_t attr;
        pthread_t first_thread;
        pthread_t second_thread;

        // Making two pointers of type
        // data_set for making again
        // call form thread
        struct data_set* info1 = new data_set;
        struct data_set* info2 = new data_set;

        // Their initialization
        info1->data = info->data;
        info2->data = info->data;

        // Initialize of pthread attribute
        pthread_attr_init(&attr);

        // For setting the set detach
        // state of attribute
        pthread_attr_setdetachstate(
            &attr, PTHREAD_CREATE_JOINABLE);

        // Partition the array for any
        // recursive call
        index = partition(info->data,
                          left_index,
                          right_index);

        info1->start_index = left_index;
        info1->end_index = index - 1;

        // Create pthread type object and
        // printing the error if any
        if (pthread_create(&first_thread,
                           &attr, quick_sort,
                           info1)) {
            cout << "Error in creating thread "
                 << endl;

            // Exiting in case of not
            // creation of thread
            exit(-1);
        }

        info2->start_index = index + 1;
        info2->end_index = right_index;

        // Creating pthread type object
        // and print the error
        if (pthread_create(&second_thread,
                           &attr, quick_sort,
                           info2)) {
            cout << "Error in creating thread "
                 << endl;

            // Exiting in case of not
            // creation of thread
            exit(-1);
        }

        // Joining the threads
        pthread_join(first_thread, NULL);
        pthread_join(second_thread, NULL);
    }

    return NULL;
}

// Driver Code
int main()
{
    // Declaration of Number of threads
    int N;

    struct data_set* info = new data_set;

    // Taking number of elements as input
    cout << "Enter number of elements"
         << " in the array: \n";
    cin >> N;

    // Declaration of array
    int A[N];

    // Initialization of array
    for (int i = 0; i < N; i++) {
        A[i] = rand() % N;
    }

    // Initialize of structure of
    // data_set type
    info->data = A;
    info->start_index = 0;
    info->end_index = N - 1;

    // Declaration of pthread object
    pthread_t thread_id;

    // Creating and pthread object and
    // printing the array of any
    if (pthread_create(&thread_id, NULL,
                       quick_sort,
                       info)) {
        cout << "Error in creating thread"
             << endl;

        // Exit in case of error
        exit(-1);
    }

    start_time = read_timer();
    // Joining the pthread object
    int r1 = pthread_join(thread_id, NULL);
    end_time = read_timer();

    // Printing the array if any in case
    // of joining
    if (r1) {
        cout << "Error in joining thread"
             << endl;

        // Exiting in case of error
        exit(-1);
    }

    cout << "Pthreads: Time: " << end_time - start_time << endl;

    // Exiting from pthread programming
    pthread_exit(NULL);


    return 0;
}

