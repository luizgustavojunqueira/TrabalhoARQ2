# TrabalhoARQ2

## Proposta

Desenvolver e/ou utilizar versões de algoritmos de ordenção implementadas nas bibliotecas OpenMP e Pthreads para avaliar o desempenho desses algoritmos (pelo menos, 3 algoritmos diferentes de ordenação) em uma máquina com, ao menos, 4 cores. 

## Configuração da Máquina utilizada

- OS: Ubuntu 22.04.4 LTS x86_64
- CPU: Intel I5-10210U (4 Cores 8 Threads) @ 1.600 GHz
- RAM: 8GB

## Algoritmos de ordenação escolhidos

- BubbleSort
    - PThreads = V 
    - OpenMP = V
    - Sequential = V
- MergeSort
    - PThreads = V
    - OpenMP = V
    - Sequential = V
- QuickSort
    - PThreads = V
    - OpenMP = V
    - Sequential = V

## Referências dos códigos utilizados

https://www.geeksforgeeks.org/implementation-of-quick-sort-using-mpi-omp-and-posix-thread/

https://github.com/ChristianMagnerfelt/ParallelQuicksort/blob/master/quicksort.c

https://github.com/dreamcrash/StackOverflow-/tree/main/OpenMP/QuickSort

https://github.com/Malhadas/Parallel-BubbleSort-/blob/master/bubble.c

https://github.com/dreamcrash/StackOverflow-/blob/main/OpenMP/MergeSort/main.c

https://stackoverflow.com/questions/52767944/merge-sort-with-pthreads-in-c#:~:text=number%20of%20threads%3A-,%23include%20%3Cstdio.h%3E,-%23include%20%3Cpthread

https://www.geeksforgeeks.org/cpp-program-for-merge-sort/?ref=lbp

https://www.geeksforgeeks.org/cpp-program-for-quicksort/

## Experimento

O tempo dos algoritmos foi medido da seguinte maneira.


Primeiramente, escolhemos 5 quantidades de elementos para o vetor a ser ordenado pelos algoritmos:

- 1000
- 10000
- 100000
- 1000000
- 10000000

Esses vetores são gerados aleatóriamente para cada execução.

Cada algoritmo foi executado 10 vezes com cada quantidade de elementos e foi utilizada a média te tempo de execuções sem segundos.
