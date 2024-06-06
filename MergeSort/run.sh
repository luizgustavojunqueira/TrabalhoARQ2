#!/bin/bash
cd OpenMP && make mergeSort && cd ..
cd PThreads && make mergeSort && cd ..
cd Sequential && make mergeSort && cd ..

DIR="TempoMaquinaLG"

rm -rf $DIR
mkdir $DIR
mkdir $DIR/1000
mkdir $DIR/10000
mkdir $DIR/25000

echo "Rodando OpenMP para 1000 numeros"
for x in {1..10}; do ./OpenMP/MergeSort < 1000.txt >> ./$DIR/1000/tempos.out; done
echo "Rodando OpenMP para 10000 numeros"
for x in {1..10}; do ./OpenMP/MergeSort < 10000.txt >> ./$DIR/10000/tempos.out; done
echo "Rodando OpenMP para 25000 numeros"
for x in {1..10}; do ./OpenMP/MergeSort < 25000.txt >> ./$DIR/25000/tempos.out; done

echo "Rodando PThreads para 1000 numeros"
for x in {1..10}; do ./PThreads/MergeSort < 1000.txt >> ./$DIR/1000/tempos.out; done
echo "Rodando PThreads para 10000 numeros"
for x in {1..10}; do ./PThreads/MergeSort < 10000.txt >> ./$DIR/10000/tempos.out; done
echo "Rodando PThreads para 25000 numeros"
for x in {1..10}; do ./PThreads/MergeSort < 25000.txt >> ./$DIR/25000/tempos.out; done

echo "Rodando Sequential para 1000 numeros"
for x in {1..10}; do ./Sequential/MergeSort < 1000.txt >> ./$DIR/1000/tempos.out; done
echo "Rodando Sequential para 10000 numeros"
for x in {1..10}; do ./Sequential/MergeSort < 10000.txt >> ./$DIR/10000/tempos.out; done
echo "Rodando Sequential para 25000 numeros"
for x in {1..10}; do ./Sequential/MergeSort < 25000.txt >> ./$DIR/25000/tempos.out; done
