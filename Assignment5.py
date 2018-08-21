#Question 1
a= int(input("Enter the year"))
flag=0
print("Enter the -1 to terminate")
while (a!=-1):
    if(a%4==0):
        if(a%100==0):
            if(a%400==0):
                print("leap year")
                flag=1
        else:
            flag=1

            print("leap year")
    if(flag==0):
        print("not a leap year")
    a=int(input("enter the year"))

#Question 2
h=input("enter height")
b=input("enter breadth")
if(h==b):
    print("sqaure")
else:
    print("rectangle")

#Question 3
age1=int(input("Age of 1 person"))
age2=int(input("Age of 2 person"))
age3=int(input("Age of 3 person"))

if(age1>age2 and age1>age3):
    if(age2>age3):
        print("oldest is 1 \nyoungest is 3")
    else:
        print("oldest is 1 \nyoungest is 2")
elif(age2>age1 and age2>age3):
    if(age1>age3):
        print("oldest is 2 \nyoungest is 3")
    else:
        print("oldest is 2 \nyoungest is 1")
else:
    if (age1>age2):
        print("oldest is 3 \nyoungest is 2")
    else:
        print("oldest is 3 \nyoungest is 1")

#Question 4
a=int(input("enter age"))
sex=input("enter sex")
st=input("enter marital status")
if (a<20 and a>60):
    if sex=='male' or sex=='female':
        print("error")
else:
    if sex=='female':
        print("u will work in urban areas only")
    else:
        if a>20 and a<40:
            print("u may work anywhere")
        else:
            print("u will work in urban areas only")
#Question 5
Quantity=int(input())
price_per_Q=100
Total=Quantity*price_per_Q
if(Total>=1000):
    print("Total amount",Total-float(Total*.1))
else:
    print("Total amount",Total)

#loops
#Question 1
li=[]
for i in range(0,10,1):
    li.append(int(input()))
print(li)

#Question 2
while True:
    print("this is an infinite while loop")

#Question 3
print("Enter the numbers sperated by space")
arr=list(map(int,input().split()))
new_list=list(map(lambda x:x*x,arr))
print(new_list)

#Question 4
li=[1,2,3,'sham','ram','0.1','0.3']
ints=[]
strs=[]
floats=[]
for i in range(0,4):
    if isinstance(li[i],int):
        ints.append(li[i])
    elif isinstance(li[i],str):
        strs.append(li[i])
    else:
        floats.append(li[i])
print(ints)
print(strs)
print(floats)

#Question 5
for i in range(1101):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)

#Question 6
for i in range(1,5):
    print('*' *i)

#Question 7
print("Enter the number sepersted by space")
arr=list(map(int,input().split()))
num=int(input())
n=arr.index(num)
del arr[n]
print(arr)

#or
print("Enter the number sepersted by space")
arr=list(map(int,input().split()))
num=int(input())
for i in range(len(arr)-1):
    if(arr[i]==num):
        del arr[i]
print(arr)
