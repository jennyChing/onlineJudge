while True:
    try:
        case_number = int(input())
        for i in range(0,case_number):
            blank = input()
            height = int(input())
            freq = int(input())
            for k in range(1,freq+1):
                for j in range(1,height+1):
                    word = str(j)
                    print(word*j)
                for j in range(height-1,0,-1):
                    word = str(j)
                    print(word*j)
                if i < case_number-1 or k < freq:
                    print()
    except(EOFError):
        break
