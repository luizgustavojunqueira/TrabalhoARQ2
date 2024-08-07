# Trabalho Prático - Arquitetura de Computadores 2

Esse repositório contém os códigos desenvolvidos para o Trabalho Pŕatico da disciplina de Arquitetura de Computadores 2 do curso de Ciência da Computação na UFMS.

## Alunos

Esse projeto foi desenvolvido pelo seguinte grupo de 3 alunos:

- [Luiz Gustavo](https://github.com/luizgustavojunqueira)
- [Camila Cardoso](https://github.com/camilacaceres1d)
- [Carlos Trindade](https://github.com/CarlosTrindade1) 

## Proposta

Desenvolver e/ou utilizar versões de algoritmos de ordenção implementadas nas bibliotecas OpenMP e Pthreads para avaliar o desempenho desses algoritmos (pelo menos, 3 algoritmos diferentes de ordenação) em uma máquina com, ao menos, 4 cores. 

## Configuração das Máquinas utilizada

- Máquina 1:
    - OS: Ubuntu 22.04.4 LTS x86_64
    - CPU: Intel I5-10210U (4 Cores 8 Threads) @ 1.600 GHz
    - RAM: 8GB

- Máquina 2:
    - Sistema Operacional: Ubuntu 22.04.4 LTS x86_64
    - Processador: AMD Ryzen 7 5700G (8 Cores e 16 Threads) @ 3.2 - 4.6 GHz
    - RAM: 16 GB

## Algoritmos de ordenação escolhidos

- BubbleSort
- MergeSort
- QuickSort

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
- 1000000 (Menos para o BubbleSort)
- 10000000 (Menos para o BubbleSort)

Esses vetores são gerados aleatóriamente para cada execução.

Cada algoritmo foi executado 10 vezes com cada quantidade de elementos para cada número de threads (2,4,8 e 16) e foi utilizada a média te tempo de execuções sem segundos
