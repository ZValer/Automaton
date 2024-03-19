# Automaton

## Description
The language I chose was all of the possible combination of 0, 1, 2 which must not have 1101, 1122, 1011 or 1012.

The modeling technique I decided to use was... to represent my solutions...

## Model of the Solution
The automata:
![image](https://github.com/ZValer/Automaton/assets/111622587/9693cf5a-20f6-4d96-929b-f9e08a9ad0d2)

The represented automata is equivalent to the following regular expression:
^(?!.*1101|.*1122|.*1011|.*1012)[012]+$

## Implementation
For my implementation of a lexical analysis, I follwed the automata as can be seen in.. fyle. To use the file you need to put the input in the format "..." and the progra should return "yes" if the string is accepted or "no" if the string is not part of the language.

Some examples of inputs and outputs are:
001122 -> yes
01010101 -> yes
011 -> yes
20120 -> yes
201112102 -> yes
001101 -> no
112210 -> no
011011 -> no
111012 -> no

## Tests
The file tests.py contains all the cases tested...

## Analysis
The complexity of my model is... 

Here is my proof by induction or hand analysis time complexity:

## References
...
