##if __name__ == '__main__':
##    n = int(input())
##    arr = map(int, input().split()) this is to take a string
## and converting it into list(.split does it) and then converting it into int. 

'''n = int(input("Enter how many scores: "))
arr = map(int, input('Enter how many scores: ').split())
arr =list(arr)

def dup(dupli):
    final_list=[]
    for num in dupli:
        if num not in final_list:
            final_list.append(num)
    return final_list

arr=dup(arr) #to remove duplicates(.remove(max())) will only remove one value not the both




arr.remove(max(arr))## return type of remove is none.

print(max(arr))

#The above code is order of n^3
---------------------------------------------------------------------------'''

n = int(input("Enter how many scores: "))
arr = map(int, input('Enter the scores: ').split()) #in 1 line arr=list(map(int, input().split()))
arr =list(arr) #to make use of n #arr1=arr[0:n]
''' for max no--
max_num=arr[0]                      
for num in range(1,len(arr)):    
    if arr[num] > max_num:
        max_num= arr[num]
#print(max_num)'''

#for 2nd max
flag=False
max_num2=arr[0]
max_num=[]
mc1=0 #max count 1
mc2=1 #maxcount 2
'''for num in range(1,len(arr)):    
    if arr[num] > max_num2:
        if arr[num] > max_num:
            max_num2=max_num
            max_num= arr[num]
        elif arr[num] == max_num:
            if arr[num+1]>max_num2:
                max_num2=arr[num+1]
print(max_num2)'''

for num in range(1, len(arr)):
    if arr[num]>max_num2:
        if not flag:    #when max_num is empty i.e for initializing
            max_num=arr[num]
            mc1=1 #to find out count of max num and max num 2
            flag=True   #now max_num is not empty
        else:
            if arr[num]>max_num:
                max_num2=max_num
                mc2=mc1 #to find out count of max num and max num 2
                max_num=arr[num]
                mc1=1 #to find out count of max num and max num 2
            elif arr[num]<max_num:
                max_num2=arr[num]
                mc2=1 #to find out count of max num and max num 2
            elif arr[num]==max_num:
                mc1=mc1+1 #to find out count of max num and max num 2
            elif arr[num]==max_num2:
                mc2=mc2+1 #to find out count of max num and max num 2
                
                
    elif arr[num]<max_num2 and not flag:
        max_num=max_num2
        max_num2=arr[num]
        mc1=mc2 #to find out count of max num and max num 2
        mc2=1 #to find out count of max num and max num 2
        flag=True
    elif arr[num]<max_num2:
        mc2=mc2
    else:
        mc2=mc2+1
    #print(max_num,max_num2,mc2)
print(max_num2, mc2, mc1)


    

