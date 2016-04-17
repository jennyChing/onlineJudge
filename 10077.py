'''
Search in Sorted Array: Binary Search
10077 - The Stern-Brocot Number System

The Stern-Brocot tree is a beautiful way for constructing the set of all nonnegative fractions m / n where m and n are relatively prime. The idea is to start with two fractions (0/1, 1/0) and then repeat the following operations as many times as desired: Insert m+m′ / n+n′ between two adjacent fractions m / n and m′/ n′.
'''
if __name__ == '__main__':
    while True:
        m_n = list(map(int, input().split()))
        m, n = m_n[0], m_n[1]
        if m and n == 1:
            break
        print(m, n)

