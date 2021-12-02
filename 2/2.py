f = open('input.txt')
moves = []
for line in f:
    splitted = line.split(sep=" ")
    moves.append({'dir':splitted[0], 'val':int(splitted[1])})
x=0
y=0
for i in range(0,len(moves)):
    if moves[i]['dir'] == 'forward':
        x+=moves[i]['val']
    if moves[i]['dir'] == 'down':
        y+=moves[i]['val']
    if moves[i]['dir'] == 'up':
        y-=moves[i]['val']
print(x)
print(y)
print(x*y)
print('------------------------------------- PART 2 -------------------------------------')
hor=0
dep=0
aim=0
for i in range(0,len(moves)):
    if moves[i]['dir'] == 'forward':
        hor+=moves[i]['val']
        dep+=moves[i]['val']*aim
    if moves[i]['dir'] == 'down':
        aim+=moves[i]['val']
    if moves[i]['dir'] == 'up':
        aim-=moves[i]['val']
print(hor)
print(dep)
print(aim)
print(hor*dep)
