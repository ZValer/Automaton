# E1 Implementation of Lexical Analysis (Automaton and Regular Expression)


## Description
##### Explaining the context of a language to perform a lexical analysis 

A language is a set, possibly infinite, of a string over some finite alphabet. Meanwhile a grammar is a way to characterize a language and list out which strings of Σ* are in the language and which are not. 

In this evidence we will do the implementation of a lexical analysis using an automaton and a regular expression. Which involves translating the rules of a language's syntax into an executable code. The parser will detect a language described as all of the possible combinations of 0, 1, 2 which must not have 1101, 1122, 1011 or 1012.

The modeling technique decided to represent the solution was a Deterministic Finite Automata (DFA). DFA is a machine composed of a finite set of states linked by arcs labeled with symbols from a finite alphabet. Each time a symbol is read, the machine changes state depending by the symbol that was read and the labeled arcs from the current state. In a DFA "there is exactly one transition from any state of finite automata for each input symbol. It accepts the string by halting at a final state, and it rejects it by halting at a non-final state." (Thakur, 2023).

Regular Expressions are another way to express a model that can accept a regular language. They are the equivalent to the automata, so any language that can be described in an automaton can also be written as a regular expression.

After the analysis, the DFA was implemented with prolog and the Regular Expression was tested with Python. This with the purpose of analyzing and implementing several different solutions for the problem to choose the most optimal depending on the time complexity and efficiency of the algorithms.


## Model of the Solution

### Automaton 
##### Generating the Automaton that recognizes the language.

A deterministic finite automaton (DFA) is a quintuple (K, Σ, q<sub>0</sub>, F, δ) where:  
- K: Finite number of states  
- Σ: Finite characters of the alphabet   
- q<sub>0</sub> ∈ K: Single designated start state
- F: Final state
- δ is a function form K x Σ to K which are the transitions (Nakayama, n.d.).


This was the automaton used to represent all the possible combination of 0, 1, 2 which must not have 1101, 1122, 1011 or 1012:
![image](https://github.com/ZValer/Automaton/assets/111622587/c7d1e578-db61-4f31-94d3-ec58336031e4)


- The nodes in the graph are states which are letters.
- The symbol in the arches represent the actions taken or the next character, in this case the next number.
- The first line represents the start.
- The double circle represents an acceptable or correct state.
- States with no double circle are not acceptable states


### Regular Expression
##### Generating a regular expression that is equivalent to the language.

The regular expression can be thought of as the algebraic description of a regular language and, as mentioned before, any language that can be described in an automaton can also be written as a regular expression. Therefore, the represented automaton is equivalent to the following regular expression:

(?!.*1101|.*1122|.*1011|.*1012)[012]+  

Breaking down the expression we have the following:

**(?!.*1101|.*1122|.*1011|.*1012)**[012]+  
( ) The parenthesis group several characters. In this case all the restrictions of the language are grouped.  

(**?!.** *1101|.*1122|.*1011|.*1012)[012]+  
?! means a Negative Lookahead where it matches if the pattern is missing (NTU, 2018).  

(?!.* **1101** |.*1122|.*1011|.*1012)[012]+  
This groups of numbers are character patterns that should be missing. 
.* Represents having any character zero or more times (NTU, 2018).  

(?!.* 1101 **|**.*1122|.*1011|.*1012)[012]+  
| is the OR Operator which matches previous OR next group of characters (Freitag, 2008).  

Summarizing **(?!.*1101|.*1122|.*1011|.*1012)**[012]+  
Is grouping the restrictions where you can't have any sequence of characters that initiate with or without a group of characters and has the specified numbers.   

(?!.*1101|.*1122|.*1011|.*1012)**[012]+**  
For the following part  
“[...]: Accept ANY ONE of the character within the square bracket” (NTU, 2018).   
+ Matches 1 or more of the previous (Freitag, 2008).  
Meaning for a match: the pattern should have 0, 1 or 2 at least one time. 

This way the regular expressions guarantees a language accepts all the possible combination of 0, 1, 2 excluding the restricted patterns 1101, 1122, 1011 and 1012.   


## Implementation

### Automaton
For my implementation of a lexical analysis, I followed the automaton as can be seen in "automaton.pl" fyle. 

> [!TIP]
> To test it in a terminal you need to go the folder with the file, write "swipl" and then "["automaton"].".
> 
>Then put the input in the format "check(number).", for example "check(001122).", and the program should return "yes" if the string is accepted or "no" if the string is not part of the language.

Some examples of inputs and outputs are:
- check([0,0,1,1,2,2]).
no
- check([0,0,1,1,2,1]).
yes
-  check([0,1,0,1,0,1,0,1]).
yes
- check([0,1,1]).
yes
- check([2,0,1,2,0]).
yes
- check(([2,0,1,1,1,2,1,0,2]).
yes
- check([0,0,1,1,0,1]).
no
- check([1,1,2,2,1,0]).
no
- check([0,1,1,0,1,1]).
no
- check([1,1,1,0,1,2]).
no


### Regular expression
(...)

## Tests

To show that the implemented model works as intended and correctly solves the problem a set of documented tests are shown. 

The file "automatonTests.pl" contains tested cases. 
> [!TIP]
>To test it in a terminal you need to go the folder with the file, write "swipl" and then "["automatonTests"].".

![image](https://github.com/ZValer/Automaton/assets/111622587/73d49cc9-cbb2-4189-8315-fbb83074f5cc)




## Analysis 

#### DFA
The complexity of my model is in general O(n). 

```
Check "Time complexity analysis.pdf" for proof of the analysis.
```

#### Regular Expression

## Conclusion
After analyzing and implementing both methods: the DFA and the Regular Expression...

On one hand, DFA..
On the other hand, Regular Expressions …


## References
Thakur, S. (2023). What Is The Difference Between DFA And NFA?. Unstop. Retrieved from: https://unstop.com/blog/difference-between-dfa-and-nfa

NTU. (2018). Regular Expressions (Regex).  NTU. Retrieved from: https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html 

Freitag, P. (2008). Regex Cheat Sheet. Petefreitag. Retrieved from: https://www.petefreitag.com/cheatsheets/regex/ 

Nakayama, M. (n. d.). CS 341: Foundations of CS II. Computer Science Department. New Jersey Institute of Technology. Retrieved from: https://web.njit.edu/~marvin/cs341/notes/chap01-handout4.pdf 
