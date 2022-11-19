
arrA = []
arrB = []


for i in range(10):
    arrA.append(int(input( str(i+1) + ": ")))


for i in range(9):
    arrB.append(arrA[i]-arrA[i+1])


print(arrB)
