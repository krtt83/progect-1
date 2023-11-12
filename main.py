# let's enter an integer
print("enter an integer")
n = int(input())
s = 1
sum = 0
# use a function for to interact the entered number
for i in range(1, n + 1):
    # sum of cubes
    sum += i ** 3
    # sum of factorials
    s *= i
print(sum, s)