with open('input') as f:
    array = [[]]
    for line in f:
        line = line.rstrip('\n')
        line = '...' + line + '...'
        array = array + [list(line)] + []

numcoords = []
symbolcoords = []
partcoords = []
total = 0

for i in range(0, len(array)):
    for j in range(0, len(array[i])):
        size = 0
        if array[i][j].isdigit() and (not array[i][j-1].isdigit() or j == 0):
            if array[i][j+1].isdigit():
                if array[i][j+2].isdigit():
                    size = 3
                else:
                    size = 2
            else: 
                size = 1
            numcoords.append([i,j, size])

# part one
for i in numcoords:
    for j in range(-1,2):
        for k in range(-1,2):
            for l in range(0, i[2]):
                try:
                    if not (array[i[0]+j][i[1]+k+l].isdigit()) and (array[i[0]+j][i[1]+k+l] != '.') and i not in partcoords:
                        i.append([i[0]+j,i[1]+k+l])
                        partcoords.append(i)
                except: pass

for i in partcoords:
    num = ''
    for j in range(0, i[2]):
        num += str(array[i[0]][i[1]+j])
    total += int(num)

print(f'Part 1: {total}')

# part two
total = 0
gearcoords = []
for i in partcoords:
    for j in partcoords:
        num1 = ''
        num2 = ''
        if j[3] == i[3] and j != i:
            for k in range(0, i[2]):
                num1 += str(array[i[0]][i[1]+k])
            for k in range(0, j[2]):
                num2 += str(array[j[0]][j[1]+k])
            total += int(num1)*int(num2)
            
print(f'Part 2: {total//2}')