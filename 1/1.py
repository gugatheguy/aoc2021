f = open("input.txt")
depths = []
for line in f:
    depths.append(int(line))
r=0
for i in range(1,len(depths)):
    if depths[i] > depths[i-1]:
        r += 1
print(r)
r=0
actualsum = depths[0] + depths[1] + depths[2]
for i in range(1,len(depths)-2):
    nextsum = depths[i] + depths[i+1] + depths[i+2]
    if nextsum > actualsum:
        r += 1
    actualsum = nextsum
print(r)
