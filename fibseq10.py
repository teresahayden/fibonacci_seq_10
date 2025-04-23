# Print the first 10 numbers of the Fibonacci sequence
x, y = 0, 1
count = 0

print("The first 10 numbers of the Fibonacci sequence:")

while count < 10:
    print(x)
    x, y = y, x + y
    count += 1
