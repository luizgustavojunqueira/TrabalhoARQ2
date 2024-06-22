#!/bin/bash
cd OpenMP && make mergeSort && cd ..
cd PThreads && make mergeSort && cd ..
cd Sequential && make mergeSort && cd ..

DIR="tempo-maquina-1"

rm -rf $DIR
mkdir $DIR

for n in {1000,10000,100000,1000000,10000000}; do
  mkdir $DIR/"$n"

  echo "Rodando Sequential para $n numeros"
  for x in {1..10}; do
    ./Sequential/MergeSort <<<"$n" >>./$DIR/"$n"/tempos.out
  done

  for numThreads in {2,4,8}; do
    echo "Rodando OpenMP para $n numeros com $numThreads threads"
    for x in {1..10}; do
      ./OpenMP/MergeSort <<<"$n $numThreads" >>./$DIR/"$n"/tempos.out
    done
    echo "Rodando PThreads para $n numeros com $numThreads threads"
    for x in {1..10}; do
      ./PThreads/MergeSort -M"$n" -T"$numThreads" >>./$DIR/"$n"/tempos.out
    done
  done
done
