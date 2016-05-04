'''
String

492 - Pig-Latin

You are to write a program that will take in an arbitrary number of lines of text and output it in Pig Latin. Each line of text will contain one or more words. A ay'' (not including the quotes) appended to it. For example, appleay''.  Words that begin with a consonant (any letter than is not A, a, E, e, I, i, O, o, U or u) should have the first consonant removed and appended to the end of the word, and then appending hello'' becomes "ellohay''.  Do not change the case of any letter.
'''
vowel = {'a', 'e', 'i', 'o', 'u'}
while True:
    try:
        content = input()
        content = content + " "
        a, b = 0, 0
        isWord = False
        isVowel = False
        for i in range(len(content)):
            if content[i].isalpha() == False and isWord == True:
                b = i
                isWord = False

                if isVowel == True:
                    print(content[a:b] + "ay", end = "")
                else:
                    print(content[a + 1:b] + content[a] + "ay", end = "")
            elif content[i].isalpha() == True and isWord == False:
                c = content[i].lower()
                a = i
                isWord = True
                if c in vowel:
                    isVowel = True
                else:
                    isVowel = False
            if content[i].isalpha() == False and i < len(content) - 1:
                print(content[i], end = "")
        print()

    except(EOFError):
        break

