#!/bin/bash

awk 'NR == 10' file.txt

#   Tests:
#1. Runtime 61 ms Beats 7.24%
#   Memory 4 MB Beats 9.60%
#2. Runtime 33 ms Beats 91.50%
#   Memory 4.1 MB Beats 9.60%