"""You are given an array of strings equations that represent relationships between
variables where each string equations[i] is of length 4 and takes one of
two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters
(not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable
names so as to satisfy all the given equations, or false otherwise.

Constraints:

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
"""
