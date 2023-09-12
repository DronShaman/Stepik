# put your python code here
n = int(input())
stroka = input()
ln = len(stroka)
for i in range(0, ln):
    s = stroka[i]
    f = ord(s) - n
    #print(f, end=" ")
    print(chr(f), end="")