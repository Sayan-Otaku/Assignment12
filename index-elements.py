d={}
n = int(input("Enter the number of elements required: - "))
d = [ map(str,raw_input().split()) for x in range(n)]

print(d)

index=int(input("Enter the index value: - "))
print(list(d)[index])
