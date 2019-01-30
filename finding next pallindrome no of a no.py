#function for pallindrome no.
def reverse(num):
    reverse= 0
    while num:
        reverse= reverse*10 + num%10
        num= num//10
    return reverse

num= int(input("Enter any number :- "))
if num==reverse(num):
    print ("Already palindrome.")
else:
    while True: #for searching next pallindrome no.
        num+= 1
        if num==reverse(num):
            print ("Next palindrome is : %s"%num)
            break
