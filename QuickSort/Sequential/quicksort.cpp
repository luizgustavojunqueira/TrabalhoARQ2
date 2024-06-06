// C++ Implementation of the Quick Sort Algorithm.
#include <iostream>
#include <sys/time.h>
#include <time.h>

using namespace std;

double start_time, end_time; /* start and end times */

double read_timer() {
  static bool initialized = false;
  static struct timeval start;
  struct timeval end;
  if (!initialized) {
    gettimeofday(&start, NULL);
    initialized = true;
  }
  gettimeofday(&end, NULL);
  return (end.tv_sec - start.tv_sec) + 1.0e-6 * (end.tv_usec - start.tv_usec);
}

int partition(int arr[], int start, int end) {

  int pivot = arr[start];

  int count = 0;
  for (int i = start + 1; i <= end; i++) {
    if (arr[i] <= pivot)
      count++;
  }

  // Giving pivot element its correct position
  int pivotIndex = start + count;
  swap(arr[pivotIndex], arr[start]);

  // Sorting left and right parts of the pivot element
  int i = start, j = end;

  while (i < pivotIndex && j > pivotIndex) {

    while (arr[i] <= pivot) {
      i++;
    }

    while (arr[j] > pivot) {
      j--;
    }

    if (i < pivotIndex && j > pivotIndex) {
      swap(arr[i++], arr[j--]);
    }
  }

  return pivotIndex;
}

void quickSort(int arr[], int start, int end) {

  // base case
  if (start >= end)
    return;

  // partitioning the array
  int p = partition(arr, start, end);

  // Sorting the left part
  quickSort(arr, start, p - 1);

  // Sorting the right part
  quickSort(arr, p + 1, end);
}

int main() {

  int N;
  // Taking number of elements as input
  cout << "Enter number of elements" << " in the array: \n";
  cin >> N;

  // Declaration of array
  int arr[N];

  // Initialization of array
  for (int i = 0; i < N; i++) {
    arr[i] = rand() % N;
  }

  start_time = read_timer();
  quickSort(arr, 0, N - 1);
  end_time = read_timer();

  cout << "Seq Time: " << end_time - start_time << endl;

  return 0;
}
