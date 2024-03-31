# Automaton

## Description
The language I chose was all of the possible combination of 0, 1, 2 which must not have 1101, 1122, 1011 or 1012.

The modeling technique I decided to use was a Deterministic Finite Automata to represent my solutions. It was easier to represent my solution because in a DFA, "there is exactly one transition from any state of finite automata for each input symbol. It accepts the string by halting at a final state, and it rejects it by halting at a non-final state." (Thakur, 2023).

## Model of the Solution
This was the automaton used to represent all the possible combination of 0, 1, 2 which must not have 1101, 1122, 1011 or 1012:
![image](https://github.com/ZValer/Automaton/assets/111622587/9693cf5a-20f6-4d96-929b-f9e08a9ad0d2)

The represented automaton is equivalent to the following regular expression:
^(?!.*1101|.*1122|.*1011|.*1012)[012]+$

## Implementation
For my implementation of a lexical analysis, I followed the automaton as can be seen in "automaton.pl" fyle. To test it in a terminal you need to go the folder with the file, write "swipl" and then "["automaton"].".

Then put the input in the format "check(number).", for example "check(001122).", and the program should return "yes" if the string is accepted or "no" if the string is not part of the language.

Some examples of inputs and outputs are:
- check(001122).
no
- check(001121).
yes
-  check(01010101).
yes
- check(011).
yes
- check(20120).
yes
- check(201112102).
yes
- check(001101).
no
- check(112210).
no
- check(011011).
no
- check(111012).
no

## Tests
The file "automatonTests.pl" contains tested cases. 
To test it in a terminal you need to go the folder with the file, write "swipl" and then "["automatonTests"].".

![image](https://github.com/ZValer/Automaton/assets/111622587/834e33e7-1a49-49e8-8e38-02d9e6348943)


## Analysis
The complexity of my model is... 

Here is my proof by induction or hand analysis time complexity:

## References
Thakur, S. (2023). What Is The Difference Between DFA And NFA?. Unstop. Retrieved from: https://unstop.com/blog/difference-between-dfa-and-nfa
