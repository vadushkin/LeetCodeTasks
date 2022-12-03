#!/bin/bash

grep '^\([0-9]\{3\}-\|([0-9]\{3\}) \)[0-9]\{3\}-[0-9]\{4\}$' file.txt


#   Tests:
#1. Runtime 136 ms Beats 30.30%
#   Memory 3.1 MB Beats 54.63%
#2. Runtime 90 ms Beats 93.49%
#   Memory 3.2 MB Beats 54.63%