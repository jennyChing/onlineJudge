while True:
    try:
        cases = int(input())
        case = 0
        for i in range(0,cases):
            numbers = list(map(int, input().split()))
            speed = 0
            case = case + 1
            for i in range(0,len(numbers)):
                if numbers[i] > speed:
                    speed = numbers[i]
            print("Case ",case,": ",speed,sep="")
    except(EOFError):
        break
