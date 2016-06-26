'''
Topological Ordering

925 - No more prerequisites, please!

Input
The first line contains the number C of test cases that follow (0 < C < 1000).  Each test case starts with a line containing the number k (0 < k ≤ 120) of courses that are to be processed. The next k lines contain the names of the k courses, one per line. The next line contains the number j of courses that have prerequisites (0 ≤ j ≤ 120). The next j lines contain, for each course that has some prerequisite, the course name, the number of prerequisites it has, and the names of the courses that are its prerequisites, separated by a single space.  Course names have maximum length 20, do not contain any spaces, and are composed of characters in the set {‘a’..‘z’}.  There are no cycles on prerequisites, that is, it is never the case that some course c has a prerequisite course cp that has c as a prerequisite (directly or indirectly).

Output
For each input case your program must output the information about the courses that have prerequisites.  Each line must contain the name of the course, the number of prerequisites it has, and the names of the courses that are its prerequisites, separated by a single space.  Within each test case, the courses must be listed ordered by name, and the list of prerequisites for each course must also be ordered by course name.
'''
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
            constrain[cons[0]] = cons[2:]
        print(course, constrain)

