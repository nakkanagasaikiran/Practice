'''
#palindrome model-1
s1=input("enter a string or number:")
#print(s1[::-1])
if(s1==s1[::-1]):
    print(s1,"is palindrome")
else:
    print(s1,"is not palindrome")
'''



'''
#palindrome model-2
no=int(input("enter a number"))
temp=no
rev=0
while(no!=0):
    r=no%10
    no=no//10
    rev=(rev*10)+r
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")
'''



'''
#prime or not
num=int(input("enter a number:"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is prime number")
    
else:
    print(num,"is not a prime number")  
'''

'''
#factorial
num=int(input("enter a number:"))
factorial=1
if(num==0):
    print("factoral of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial of",num,"is",factorial)
'''

'''
#Tables
no=int(input("enter a number:"))
for i in range(1,21):
    print(no,'*',i,'=',no*i)
'''

'''
#fibonacci series
nterms=int(input("enter no of terms:"))
a=0
b=1
if(nterms==1):
    print("fibonacci series:",a)
else:
    for i in range(nterms):
        print(a,end=' ')
        c=a+b
        a=b
        b=c
        
'''



        
        
