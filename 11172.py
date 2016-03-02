while True:
   try:
       pair_count = int(input())
       for i in range(0, pair_count):
               value = list(map(int, input().split()))
               if value[0] > value[1]:
                       print('>')
               elif value[0] < value[1]:
                       print('<')
               else:
                       print('=')
   except(EOFError):
       break
