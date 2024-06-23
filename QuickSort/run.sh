#!/bin/bash
cd OpenMP && make quickSort && cd ..
cd PThreads && make quickSort && cd ..
cd Sequential && make quickSort && cd ..

DIR="tempo-maquina-1"

rm -rf $DIR
mkdir $DIR

for n in {1000,10000,100000,1000000,10000000}; do
  mkdir $DIR/"$n"

  echo "Rodando Sequential para $n numeros"
  for x in {1..10}; do
    ./Sequential/QuickSort <<<"$n" >>./$DIR/"$n"/tempos.out
  done

  for numThreads in {2,4,8}; do
    echo "Rodando OpenMP para $n numeros com $numThreads threads"
    for x in {1..10}; do
      ./OpenMP/QuickSort "$n" 0 "$numThreads" >>./$DIR/"$n"/tempos.out
    done
    echo "Rodando PThreads para $n numeros com $numThreads threads"
    for x in {1..10}; do
      ./PThreads/QuickSort "$n" "$numThreads" >>./$DIR/"$n"/tempos.out
    done
  done
done
