#!/bin/bash

DIR="TempoMaquinaLG"

make bubbleSort

rm -rf $DIR
mkdir $DIR
mkdir $DIR/1000
mkdir $DIR/10000
mkdir $DIR/25000

echo "Rodando para 1000 numeros"
for x in {1..10}; do ./BubbleSort 1000 g 4 >> ./$DIR/1000/tempos.out; done
echo "Rodando para 10000 numeros"
for x in {1..10}; do ./BubbleSort 10000 g 4 >> ./$DIR/10000/tempos.out; done
echo "Rodando para 25000 numeros"
for x in {1..10}; do ./BubbleSort 25000 g 4 >> ./$DIR/25000/tempos.out; done
