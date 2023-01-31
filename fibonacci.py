n=int(input("Enter the number of terms: "))
n1 = 0
n2 = 1
print(n1)
print(n2)
for x in range(1,n):
    n3 = n1 + n2
    print(n3)
    n1,n2=n2,n3
