import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_1.sort()
names_2.sort()

duplicates = []
a = 0
b = 0
while a < len(names_1) and b < len(names_2):
    if names_1[a] == names_2[b]:
        duplicates.append(names_1[a])
        a += 1
        b += 1
    elif names_1[a] < names_2[b]:
        a += 1
    else:
        b += 1


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

