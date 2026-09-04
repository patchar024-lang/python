L = [2,5,9,7,65,72, 34, 23, 12, 45]
print("Original List:", L)
count = 0
for i in L:
    count +=1
avg = count / len(L)
print("sum =", count)
print("average =", avg)

L. sort()

print("the smallest element is:", L[0])

print("the largest element is:", L[-1])