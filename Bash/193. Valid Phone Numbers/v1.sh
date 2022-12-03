#!/bin/bash

awk '/^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$/' file.txt


#   Tests:
#1. Runtime 140 ms Beats 23.4%
#   Memory 3.9 MB Beats 6.82%
#2. Runtime 100 ms Beats 83.33%
#   Memory 3.8 MB Beats 6.82%