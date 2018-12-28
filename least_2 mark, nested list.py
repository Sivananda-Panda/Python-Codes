list_item=[]
for i in range(int(input())):
    temp=[]
    name=input()
    score=float(input())
    temp.append(name) #u can try directly also like temp.append(input('name'))
    temp.append(score)#for inner list
    list_item.append(temp)#for outer list
#print(list_item)


#now calculate the 2nd highest rank according to the mark
flag = False
least_1=[]
least_2=list_item[0][1]

for marks in range(1,len(list_item)):
    if list_item[marks][1]>least_2:
        if not flag:
            least_1=least_2
            least_2=list_item[marks][1]
            flag=True
        '''else:
            if list_item[marks][1]>max_1:
                max_2=max_1
                max_1=max_2

            elif list_item[marks][1]<max_1:
                max_2=list_item[marks][1]'''
                
    elif list_item[marks][1]<least_2:
        if not flag:
            least_1=list_item[marks][1]
            flag=True
        else:
            if list_item[marks][1]<least_1:
                least_2=least_1
                least_1=list_item[marks][1]
            elif list_item[marks][1]>least_1:
                least_2=list_item[marks][1]

names=[]
for i in range(0,len(list_item)):
    ct=0
    if list_item[i][1]==least_2:
        names.insert(ct,list_item[i][0])
        ct=ct+1
names.sort()
for item in names:
    print(item)
'''print(names)'''
