'''
SequenceManipulation - select

11875 - Brick Game
There is a village in Bangladesh, where brick game is very popular. Brick game is a team game. Each team consists of odd number of players. Number of players must be greater than 1 but cannot be greater than 10. Age of each player must be within 11 and 20. No two players can have the same age.  There is a captain for each team. The communication gap between two players depends on their age difference, i.e. the communication gap is larger if the age difference is larger. Hence they select the captain of a team in such a way so that the number of players in the team who are younger than that captain is equal to the number of players who are older than that captain.  Ages of all members of the team are provided. You have to determine the age of the captain.

Input
Input starts with an integer T (T ≤ 100), the number of test cases.  Each of the next T lines will start with an integer N (1 < N < 11), number of team members followed by N space separated integers representing ages of all of the members of a team. Each of these N integers will be between 11 and 20 (inclusive). Note that, ages will be given in strictly increasing order or strictly decreasing order. We will not mention which one is increasing and which one is decreasing, you have to be careful enough to handle both situations.

Output
For each test case, output one line in the format ‘Case x: a’ (quotes for clarity), where x is the case number and a is the age of the captain.
'''
def kth(team,k):
    p = team[0]
    L = []
    R = []
    for i in range(1,len(team)):
        if p > team[i]:
            L.append(team[i])
        else:
            R.append(team[i])
    if len(L) == k - 1:
        return p
    if len(L) >= k:
        return kth(L, k)
    return kth(R, k - len(L) - 1)

if __name__ == '__main__':
    case = 0
    cases = int(input())
    for _ in range(cases):
        case += 1
        team = list(map(int, input().split()))
        team = team[1:]
        # if len(team) is odd: do kth twice
        if len(team)%2:
            print("Case ", case, ": ", kth(team, len(team) // 2 + 1), sep = "")
        else:
            print("Case ", case, ": ", ((kth(team, len(team) // 2)) + kth(team, len(team) // 2 + 1)) // 2, sep = "")

