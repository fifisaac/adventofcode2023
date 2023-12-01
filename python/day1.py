def check_word(line,i,sign):
    strings =   {'one':1,
                'two':2,
                'three':3,
                'four':4,
                'five':5,
                'six':6,
                'seven':7,
                'eight':8,
                'nine':9}
    word = ''
    # i should not be allowed to use a computer
    try:
        if sign == '+':
            if (line[i] + line[i+1] + line[i+2]) in strings:
                word += str(strings[line[i] + line[i+1] + line[i+2]])
            elif (line[i] + line[i+1] + line[i+2] + line[i+3]) in strings:
                word += str(strings[line[i] + line[i+1] + line[i+2] + line[i+3]])
            elif (line[i] + line[i+1] + line[i+2] + line[i+3] + line[i+4]) in strings:
                word += str(strings[line[i] + line[i+1] + line[i+2] + line[i+3] + line[i+4]])
        else:
            if (line[-i-3] + line[-i-2] + line[-i-1]) in strings:
                word += str(strings[line[-i-3] + line[-i-2] + line[-i-1]])
            elif (line[-i-4] + line[-i-3] + line[-i-2] + line[-i-1]) in strings:
                word += str(strings[line[-i-4] + line[-i-3] + line[-i-2] + line[-i-1]])
            elif (line[-i-5] + line[-i-4] + line[-i-3] + line[-i-2] + line[-i-1]) in strings:
                word += str(strings[line[-i-5] + line[-i-4] + line[-i-3] + line[-i-2] + line[-i-1]])
    except:
        pass

    return word


def pt1():
    total = 0
    with open('input') as file:
        for line in file:
            right = ''
            left = ''

            for i in range(0, len(line)):

                if line[i].isdigit() and left == '':
                    left = line[i]
                elif check_word(line,i,'+').isdigit() and left == '':
                    left = check_word(line,i,'+')
                if line[-i-1].isdigit() and right == '':
                    right = line[-i-1]
                elif check_word(line,i,'-').isdigit() and right == '':
                    right = check_word(line,i,'-')
            total += int( left + right )

    return total

print(pt1())
