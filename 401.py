m = {'E':'3','3':'E','L':'J','J':'L','S':'2','2':'S','5':'Z','Z':'5'}
sym = ['A','H','I','M','O','T','U','V','W','X','Y','1','8']
non = ['B','C','D','F','G','K','N','P','Q','R','4','6','7','9']
while True:
    try:
        isPal,isMirr = None, None
        content = input()
        for i in range(0,len(content)):
            if len(content) == 1 and content[i] in (sym or m):
                isPal,isMirr = True, True
                break
            if content[i] == content[len(content)-1-i]:
                if isPal == None:
                    isPal = True
                if isMirr == None:
                    isMirr == True
                if (content[i] in m and content[i]==content[len(content)-1-i]) or content[i] in non:
                    isMirr = False
                #print(content[i],content[len(content)-1-i],isPal,isMirr)
            elif content[i] in m and m[content[i]]==content[len(content)-1-i]:
                isMirr = True
                isPal = False
                #print(content[i],content[len(content)-1-i],isPal,isMirr)
            else:
                isPal, isMirr = False, False
                #print(content[i],content[len(content)-1-i],isPal,isMirr)
                break
        if isPal == False and isMirr == False:
            print(content,"-- is not a palindrome.")
        elif isPal == True and (isMirr == None or isMirr == True):
            print(content,"-- is a mirrored palindrome.")
        elif isPal == True and isMirr == False:
            print(content,"-- is a regular palindrome.")
        elif isMirr == True and isPal == False:
            print(content,"-- is a mirrored string.")
        print()
    except(EOFError):
        break

