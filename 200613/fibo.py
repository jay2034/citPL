first = 1
second = 1

print(first)
print(second)

while( second < 100000):
    temp = first
    first = second
    second = temp + second
    print(second)
