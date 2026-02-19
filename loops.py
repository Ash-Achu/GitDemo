#if else condition

greeting = "Good Morning"
a = 4

if greeting == "Good Morning":
    print("Condition matches")
    print("second line")
else:
    print("Condition not matches")
print("if else condition is completed")

if a > 2 :
    print("Condition matches")
    print("second line")
else:
    print("Condition not matches")
print("if else condition is completed")

#for loop

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i)
#To print multiples of 2
for i in obj:
    print(i*2)
#To print the sum of first five natural numbers

for j in range(1,6):
    print(j)

summation = 0
for j in range(1,6):
    summation = summation + j
print(summation)

#To print in increment of 2
for k in range(1,10,2):
    print(k)
#If no increment value or range is given it will print from 0 to n-1
for m in range(10):
    print(m)



