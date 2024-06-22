#!/bin/bash

DIR="tempo-maquina-1"

make bubbleSort

rm -rf $DIR
mkdir $DIR

for n in {1000,10000}; do
  mkdir $DIR/"$n"
  echo "Rodando para $n numeros com 2 threads"
  for x in {1..10}; do ./BubbleSort "$n" g 2 1 >>./$DIR/"$n"/tempos.out; done
  for numThreads in {4,8}; do
    echo "Rodando para $n numeros com $numThreads threads"
    for x in {1..10}; do ./BubbleSort "$n" g "$numThreads" 0 >>./$DIR/"$n"/tempos.out; done
  done
done

n=100000
mkdir $DIR/"$n"
echo "Rodando para $n numeros com 2 threads"
./BubbleSort "$n" g 2 1 >>./$DIR/"$n"/tempos.out
for numThreads in {4,8}; do
  echo "Rodando para $n numeros com $numThreads threads"
  ./BubbleSort "$n" g "$numThreads" 0 >>./$DIR/"$n"/tempos.out
done
