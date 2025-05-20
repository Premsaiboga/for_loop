# write 1 to 10 sum of odd
a = 10
b = 0
for i in range(1,a+1):
    if i%2 != 0:
       b += i
print(b) 

#write 1 to 10 sum of even
c= 10
d = 0
for i in range(1,c+1):
    if i%2 == 0:
       d+=i
print(d)

#write 1 to 10 sum of digits
e = 10
f = 0
for i in range(1,e+1):
      f+=i
print(f) 

#greater value of 2 numbers
g =int(input("enter first number: "))
h =int(input("enter second number: "))
if g>h:
    print("G is the gratest number")
else:
    print("H is the greatest number")

#greater valu of 3 numbers
x=int(input("enter first number: "))
y=int(input("enter second number: "))
z= int(input("enter third number: "))
if x>y and x>z:
    print("x is the greatest value i.e",x)
elif y>x and y>z:
    print("y is the greatest value i.e,", y)
else:
    print("z is the greatest value i.e,",z)

#prime numbers for 1 to 10
for num in range(1, 11):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

#leap year
year = int(input("enter a year:"))
if year%400 ==0 and year%100 ==0:
    print("its a leap year")
elif year%4 ==0 and year%100!=0:
    print("its a leap year")
else:
    print("it's not a leap year")

