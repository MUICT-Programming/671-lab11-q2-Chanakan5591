n = int(input())

lst1 = []
lst2 = []

for _ in range(n):
    lst1.append(int(input()))

for _ in range(n):
    lst2.append(int(input()))

def summation(lst1, lst2):
    return [a+b for a,b in zip(lst1, lst2)]

def find_min_max(lst):
    return (min(lst), max(lst))

sum_result = summation(lst1, lst2)
min_max = find_min_max(sum_result)

print(sum_result)
print(min_max)
