while True:
    try:
        cases = int(input())
        for i in range(0, cases):
            pairs = input()
            isPair = True
            a = []
            for c in pairs:
                if c == "(" or c == "[":
                    a.append(c)
                elif c == ")" or c == "]":
                    if not a or (c==")" and a[-1]!="(") or (c=="]" and a[-1]!="[") :
                        isPair=False
                        break
                    elif (c=="]" and a[-1]=="[") or (c==")" and a[-1]=="("):
                        a.pop()
            if a or isPair == False:
                print("No")
            else:
                print("Yes")
    except(EOFError):
        break

