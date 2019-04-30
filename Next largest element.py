#code

t=int(input())
for j in range(t):
    length=int(input())
    li=list(map(int, input().split()))
    li2=[]
    for i in range(len(li)):
        c=1
        
        if (i+c)<len(li):  
            while ((i+c)<len(li)) and (li[i+c]<li[i]):
                #if li[i]==li2[-1]:
                    #li2.append(-1)
                c=c+1
                #if ((i+c)<len(li)):
                    #break
                if (i+c)==len(li):
                    #li2.append(-1)
                    c=0
                    break
            if li[i+c]>li[i]:
                li2.append(li[i+c])
            elif li[i+c]==li[i]:
                li2.append(-1)
            elif li[i+c]<li[i]:
                li2.append(-1)
        else:
            li2.append(-1)
    for i in li2:
        print(i, end=' ')
    print('')
#code
#code
t=int(input())
for i in range(t):
    length=int(input())
    li=list(map(int, input().split()))
    sta=[]
    res=[]
    for i in range(len(li)):
        flag=False
        while(len(sta)!=0):
            if li[i]>sta[-1]:
                sta.pop(len(sta)-1)
                res.append(li[i])
                flag=True
            elif li[i]==sta[-1]:
                sta.pop(len(sta)-1)
                res.append(-1)
                flag=True
            else:
                sta.append(li[i])
                break
        if flag:
            sta.append(li[i])
        if len(sta)==0:
            sta.append(li[i])
        
            
        c=len(sta)
        if c==len(li):
            while c:
                print(-1, end=' ')
                c=c-1
        elif i==len(li)-1 and c!=0:
            sta.pop(len(sta)-1)
            res.append(-1)
    for i in res:
        print(i, end=' ')
    print()
#from office
#code
t=int(input())
for i in range(t):
    def gl():
        length=int(input())
        li=list(map(int, input().split()))
        li2=[]
        res=[]
        '''for i in range(length):
            res.append(0)'''
        
        for i in range(len(li)):
            flag=False
            while (len(li2)!=0 and li[i]>li2[-1]):
                res.insert(li.index(li2[-1]), li[i])
                li2.pop(len(li2)-1)
                flag=True
            if flag:
                li2.append(li[i])
            
            if (len(li2)==0):
                li2.append(li[i])
            elif li[i]<li2[-1]:
                li2.append(li[i])
        
        c=len(li2)
        while (c!=0):
            res.insert(li.index(li2[-1]), -1)
            c=c-1
        return res
    res1=gl()
    for j in res1:
        print(j, end=' ')
    print()
#final
t=int(input())
for i in range(t):
    length=int(input())
    li=list(map(int, input().split()))
    sta=[]
    res=[]
    for i in range(len(li)):
        flag=False
        while(len(sta)!=0):
            if li[i]>sta[-1]:
                
                res.insert(li.index(sta[-1]), li[i])
                sta.pop(len(sta)-1)
                
                flag=True
            elif li[i]==sta[-1]:
                res.insert(li.index(sta[-1]), -1)
                sta.pop(len(sta)-1)
                
                flag=True
            elif li[i]<sta[-1]:
                sta.append(li[i])
                flag=False
                break
        if flag:
            sta.append(li[i])
        if len(sta)==0:
            sta.append(li[i])
        
            
        c=len(sta)
        if c==len(li):
            while c:
                res.insert(li.index(sta[-1]), -1)
                c=c-1
        elif i==len(li)-1 and c!=0:
            while len(sta)!=0:
                res.insert(li.index(sta[-1]), -1)
                sta.pop(len(sta)-1)
            
    for i in res:
        print(i, end=' ')
    print()
