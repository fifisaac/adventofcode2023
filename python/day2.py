def pt1():
    total = 0
    with open('input') as f:
        for line in f:
            array = line.replace('blue', 'b').replace('green', 'g').replace('red', 'r').replace(' ', '').lstrip('Game').replace(':', ',').replace(';', ',').rstrip('\n').split(',')
            for i in array:
                blue = 0
                green = 0
                red = 0
                invalid = False
                if 'b' in i:
                    if int(i.rstrip('b')) > 14:
                        invalid = True
                        break
                if 'g' in i:
                    if int(i.rstrip('g')) > 13:
                        invalid = True
                        break
                if 'r' in i:
                    if int(i.rstrip('r')) > 12:
                        invalid = True
                        break
            if not invalid:
                total += int(array[0])

        return total

def pt2():
    total = 0
    with open('input') as f:
        for line in f:
            blue = 0
            green = 0
            red = 0
            array = line.replace('blue', 'b').replace('green', 'g').replace('red', 'r').replace(' ', '').lstrip('Game').replace(':', ',').replace(';', ',').rstrip('\n').split(',')
            for i in array:
                if 'b' in i:
                    if int(i.rstrip('b')) > blue:
                        blue = int(i.rstrip('b'))
                if 'g' in i:
                    if int(i.rstrip('g')) > green:
                        green = int(i.rstrip('g'))
                if 'r' in i:
                    if int(i.rstrip('r')) > red:
                        red = int(i.rstrip('r'))
            power = red*green*blue
            total += power

        return total

print(pt1())
print(pt2())
