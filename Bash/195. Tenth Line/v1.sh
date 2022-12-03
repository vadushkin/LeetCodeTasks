#!/bin/bash

count=0
while read line && [ $count -le 10 ]
do
  let 'count = count + 1'

  if [ "$count" -eq 10 ]
  then
    echo "$line"
    exit 0
  fi

done <file.txt

#   Tests:
#1. Runtime 45 ms Beats 57.85%
#   Memory 3.5 MB Beats 83.8%
#2. Runtime 33 ms Beats 91.50%
#   Memory 3.6 MB Beats 83.8%