# for i  in range(10):
#     print(i)

# print(5* "-----------")
# for i in range(2, 10):
#     print(i)

for i in range(2, 20, 2):
    print(i)

print(5* "-----------")

for i in range(20, 2, -2):
    print(i)

print(5 * "-----------")

for i in range(2, 20, 2):
    if (i % 4 == 0):
        print(i)

print(5 * "-----------")


for j in range(3, 30, 3):
    print(j)

print(5 * "-----------")

# zip is used to group  different data range into a itratable touple object

for i, j in zip(range(2, 20, 2), range(2, 20, 3)):
    print(f" i, j -> {i} {j}")

# d   =  [ a for a in  zip(range(2,20, 2), range(2, 20 , 3)) ]
# print(d)

print(5 * "-----------")

j = 20
while True:
    if (j == 0):
        break
    print(j)
    j -= 1
