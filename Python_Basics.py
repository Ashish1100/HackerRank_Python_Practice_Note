#1. Printing Hello World:
#printing anthing(Hello, World!)here in python
#->denotes comments

print("Hello, World!")



#2 if-else:
#Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

input("Enter the number", n);
if n%2==1:
    print("weird");
elif n%2==0 & n>=2 & n<=5:
    print("Not Weird");
elif n%2==0 & n>=6 & n<=20:
    print("Weird");
elif n%2==0 & n>20:
    print("Not Weird");
    

#3. Arithmetic Operators
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
        
x=int(input())
y=int(input())
print(x+y)
print(x-y)
print(x*y)


#4. Division
a=float(input())
b=float(input())
print(a//b)
print(a/b)


#5. Loops:

x=int(input())

for i in range(x):
    print(i*i)


    
#6. Functions:
def pn(x):
    for i in range(x):
        print(i+1,end="")

x=int(input())
pn(x)



#7. Finding Leap Year using python functions:
def is_leap(year):
    leap = False
    if year%400==0:
        leap=True
    elif year%100==0:
       leap=False
    elif year%4==0:
        leap=True   
    
    return leap

year = int(input())
