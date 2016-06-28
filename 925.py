'''
Topological Ordering

925 - No more prerequisites, please!

Input
The first line contains the number C of test cases that follow (0 < C < 1000).  Each test case starts with a line containing the number k (0 < k ≤ 120) of courses that are to be processed. The next k lines contain the names of the k courses, one per line. The next line contains the number j of courses that have prerequisites (0 ≤ j ≤ 120). The next j lines contain, for each course that has some prerequisite, the course name, the number of prerequisites it has, and the names of the courses that are its prerequisites, separated by a single space.  Course names have maximum length 20, do not contain any spaces, and are composed of characters in the set {‘a’..‘z’}.  There are no cycles on prerequisites, that is, it is never the case that some course c has a prerequisite course cp that has c as a prerequisite (directly or indirectly).

Output
For each input case your program must output the information about the courses that have prerequisites.  Each line must contain the name of the course, the number of prerequisites it has, and the names of the courses that are its prerequisites, separated by a single space.  Within each test case, the courses must be listed ordered by name, and the list of prerequisites for each course must also be ordered by course name.

Solution
Find one course's prerequisites and delete all its prerequisites
只 care 先修課的先修課是否出現在他所有的 prerequisites 中
不能只比較兩層，因為上一層 pre 中不一定會列出全部的先修課！
'''
def DFS(constrain):
    for k, v in constrain.items():
        for c in v:
            if c in constrain:
                temp = constrain[k].union(constrain[c]).copy()
                print(temp, constrain[k], constrain[c])
                v = temp

def delete_repeat(course, constrain):
    result = {}
    for pre in constrain[course]:
        #print(pre)
        result[course] = set()
        if pre in constrain:
         #   print(pre, course, constrain[pre], constrain[course], constrain[course].difference_update(constrain[pre]), constrain[pre].difference_update(constrain[course]))
            A = constrain[course].copy()
            B = constrain[pre].copy()
            A.difference_update(B)
            result[course] = A.copy()
            #print(course, pre, constrain[course], constrain[pre], "R:", result)
        else:
            result[course] = constrain[course]
    return result[course].copy()

if __name__ == '__main__':
    case = int(input())
    course = []
    for _ in range(case):
        k = int(input())
        for i in range(k):
            c = input()
            course.append(c)
        j = int(input())
        constrain = {}
        for x in range(j):
            cons = list(map(str, input().split()))
            constrain[cons[0]] = set(cons[2:])
        #DFS(constrain)
        #print(course, constrain)
        result = {}
        for k, v in constrain.items():
            temp = delete_repeat(k, constrain)
            result[k] = temp
            #print(k, temp)
        print(result)
        print()

