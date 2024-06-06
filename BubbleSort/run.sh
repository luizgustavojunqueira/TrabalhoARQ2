#!/bin/bash
COMPILADO=$(ls | grep "BubbleSort") 

if [ "$COMPILADO" = "" ]; then
    $(make bubbleSort)  
fi

$(rm -rf ./1000 && mkdir 1000)
$(rm -rf ./10000 && mkdir 10000)
$(rm -rf ./25000 && mkdir 25000)

for x in {1..10}; do $(./BubbleSort 1000 g 4 >> ./1000/tempos.out); done
for x in {1..10}; do $(./BubbleSort 10000 g 4 >> ./10000/tempos.out); done
for x in {1..10}; do $(./BubbleSort 25000 g 4 >> ./25000/tempos.out); done
