with open('input') as f:
    time = f.readline().split()
    distances = f.readline().split()
    f.seek(0,0)
    time2 = f.readline().replace(' ', '').rstrip('\n').split(':')
    distances2 = f.readline().replace(' ', '').rstrip('\n').split(':')


def main(time, distances):
    totalarr = []
    total = 1

    for i in range(1,len(time)):
        temptotal = 0
        for j in range(0,int(time[i])):
            speed = j
            distance = (int(time[i]) - j) * j
            if distance > int(distances[i]):
                temptotal += 1
        totalarr.append(temptotal)

    for i in totalarr:
        total = total * i
    
    return(total)

print(main(time, distances))
print(main(time2, distances2))