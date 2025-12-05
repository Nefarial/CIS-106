n = 20

a = 1  
b = 1  
print(a, end=" ")
print(b, end=" ")

for _ in range(3, n + 1):
    c = a + b
    print(c, end=" ")
    a, b = b, c

print() 
