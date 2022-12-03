#!/bin/bash

tail -n+10 file.txt | head -1


#   Tests:
#1. Runtime 54 ms Beats 18.39%
#   Memory 3.6 MB Beats 41.25%
#2. Runtime 38 ms Beats 80.23%
#   Memory 3.5 MB Beats 83.8%