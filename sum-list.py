def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
lst=list()
n = int(input("Enter the number of items in list: - "))
for i in range(n):
    lst.append(int(input()))
print(sum_list(lst))
