s=input()
c=0
if len(s)==1:
    print(0)

elif s[:]==s[::-1]:
    for i in s:
        if s[0]==i:
            c=c+1
    if c==len(s):
        print(0)
    else:
        print(len(s)-1)
    
else:
    print(len(s))
