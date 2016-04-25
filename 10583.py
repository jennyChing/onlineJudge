'''
Set - Disjoint-sets Forest

10583 - Ubiquitous Religions

Input
The input consists of a number of cases. Each case starts with a line specifying the integers n and m. The next m lines each consists of two integers i and j, specifying that students i and j believe in the same religion. The students are numbered 1 to n. The end of input is specified by a line in which n = m = 0.

Output
For each test case, print on a single line the case number (starting with 1) followed by the maximum number of different religions that the students in the university believe in.

Solution:
    For each pair of students, add them to the same group. Return the number of groups at the end
'''
if __name__ == '__main__':
    while True:
        try:
            cases = 1
            n, m = list(map(int, input().split()))
            student = {}
            groups = {}
            group_cnt = 0
            if n == 0 and m == 0:
                break
            for pairs in range(m):
                p = list(map(int, input().split()))
                l, r = p[0] - 1, p[1] - 1
# both already exists in two different groups: combine the two to the group with smaller index
                if l in student and r in student and student[l] != student[r]:
                    #print(student, groups)
                    temp = groups[student[r]].copy()
                    delete = student[r]
                    groups[student[l]].update(temp)
                    for key, value in student.items():
                        if value == delete:
                            student[key] = student[l]
                    groups[delete] = set()
# one exist and the other does not: add the new one into the same group
                elif l in student and r not in student:
                    student[r] = student[l]
                    groups[student[l]].add(r)
                elif l not in student and r in student:
                    student[l] = student[r]
                    groups[student[r]].add(l)
# both doesn't exits: open a new group and add both into the new group
                elif l not in student and r not in student:
                    groups[group_cnt] = set()
                    groups[group_cnt].add(l)
                    groups[group_cnt].add(r)
                    student[l] = student[r] = group_cnt
                    group_cnt += 1
            all_students = set()
            students = set()
            for i in range(n):
                all_students.add(i)
            for key, value in student.items():
                students.add(key)
            remain = all_students - students
            print("Case ", cases, ": ", len(groups) + len(remain), sep = "")
            cases += 1
        except(EOFError):
            break


