#!/bin/bash
cd OpenMP && make quickSort && cd ..
cd PThreads && make quickSort && cd ..
cd Sequential && make quickSort && cd ..

DIR="TempoMaquinaLG"

rm -rf $DIR
mkdir $DIR
mkdir $DIR/1000
mkdir $DIR/10000
mkdir $DIR/25000

echo "Rodando OpenMP para 1000 numeros"
for x in {1..10}; do ./OpenMP/QuickSort < 1000.txt >> ./$DIR/1000/tempos.out; done
echo "Rodando OpenMP para 10000 numeros"
for x in {1..10}; do ./OpenMP/QuickSort < 10000.txt >> ./$DIR/10000/tempos.out; done
echo "Rodando OpenMP para 25000 numeros"
for x in {1..10}; do ./OpenMP/QuickSort < 25000.txt >> ./$DIR/25000/tempos.out; done

echo "Rodando PThreads para 1000 numeros"
for x in {1..10}; do ./PThreads/QuickSort < 1000.txt >> ./$DIR/1000/tempos.out; done
echo "Rodando PThreads para 10000 numeros"
for x in {1..10}; do ./PThreads/QuickSort < 10000.txt >> ./$DIR/10000/tempos.out; done
echo "Rodando PThreads para 25000 numeros"
for x in {1..10}; do ./PThreads/QuickSort < 25000.txt >> ./$DIR/25000/tempos.out; done

echo "Rodando Sequential para 1000 numeros"
for x in {1..10}; do ./Sequential/QuickSort < 1000.txt >> ./$DIR/1000/tempos.out; done
echo "Rodando Sequential para 10000 numeros"
for x in {1..10}; do ./Sequential/QuickSort < 10000.txt >> ./$DIR/10000/tempos.out; done
echo "Rodando Sequential para 25000 numeros"
for x in {1..10}; do ./Sequential/QuickSort < 25000.txt >> ./$DIR/25000/tempos.out; done
