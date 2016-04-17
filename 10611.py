'''
sort - Binary Search
10611 - The Playboy Chimp

Luchu was looking for the tallest lady chimp that would be shorter than he; he would also like to consider someone a little taller than he. But someone of his same height will never be on his list. Every morning Luchu picks up a line of lady chimps and finds the best two according to his set criterion. His job has been made easy by the fact that the lady chimps in each line are ordered by their height, the shortest one is in the front and the tallest one is at the back. Your task is to help Luchu on one particular day to find two lady chimps: the tallest one shorter than he and the shortest one taller than he.

Sample Input
4 # number of lady chimps
1 4 5 7 # height of all the lady chimps in asending order
4 # number of querys
4 6 8 10 # the heights of luchu

Sample Output
1 5 # first is the tallest chimp shorter then Luchu; second is the shortest taller
5 7
7 X
7 X
'''
# start from comparing the height in the middle and n every time, if fits the criteria, save the middle value as temp answer and move the range to the one next to middle. If there is no candidates left, return the last temp answer

def tallShortest (ladies, n):
    l, r = 0, len(ladies) - 1
    temp = None
    while r >= l:
        m = (l + r) // 2
        if n >= ladies[m]:
            l = m + 1
        else:
            temp = ladies[m]
            r = m - 1
    if temp == None: temp = 'X'
    return temp

def shortTallest (ladies, n):
    l, r = 0, len(ladies) - 1
    temp = None
    while r >= l:
        m = (l + r) // 2
        if n <= ladies[m]:
            r = m - 1
        else:
            temp = ladies[m]
            l = m + 1
    if temp == None: temp = 'X'
    return temp

if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            ladies = list(map(int, input().split()))
            Q = int(input())
            queries = list(map(int, input().split()))
            for n in queries:
               print(shortTallest(ladies, n), tallShortest(ladies, n))
        except(EOFError):
            break


