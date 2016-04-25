'''
set - Disjoint-sets Forest

793 - Network Connections
Input
The input begins with a single positive integer on a line by itself, indicating the number of the cases following. This line is followed by a blank line, and there is also a blank line between two consecutive inputs.
For each test case, the input must follow the description below.
1. The number of computers in the network (a strictly positive integer);
2. A list of pairs of the form:
    (a) c computeri computerj , where computeri and computerj are integers from 1 to no of computers.  A pair of this form shows that computeri and computerj get interconnected.
    (b) q computeri computerj , where computeri and computerj are integers from 1 to no of computers.  A pair of this form stands for the question: is computeri interconnected with computerj ?
    Each pair is on a separate line. Pairs can appear in any order, regardless of their type. The log is updated after each pair of type (a) and each pair of type (b) is processed according to the current network configuration.

Output
    For each test case, the output must follow the description below. The outputs of two consecutive cases will be separated by a blank line.  The program prints two integer numbers to the standard output on the same line, in the order: ‘successful answers, unsuccessful answers’, as shown in the sample output.

Note:
    For example, the first input illustrated in the sample below corresponds to a network of 10 computers and 7 pairs. There are ‘1’ successfully answered questions and ‘2’ unsuccessfully answered questions.
