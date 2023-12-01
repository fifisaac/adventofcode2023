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
    # code from hell
    try:
        if sign == '+':

            threeletter = (line[i] + line[i+1] + line[i+2])
            fourletter = (line[i] + line[i+1] + line[i+2] + line[i+3])
            fiveletter = (line[i] + line[i+1] + line[i+2] + line[i+3] + line[i+4])

            if threeletter in strings:
                word = threeletter
            elif fourletter in strings:
                word = fourletter
            elif fiveletter in strings:
                word = fiveletter

        else:

            threeletter = (line[-i-3] + line[-i-2] + line[-i-1])
            fourletter = (line[-i-4] + line[-i-3] + line[-i-2] + line[-i-1])
            fiveletter = (line[-i-5] + line[-i-4] + line[-i-3] + line[-i-2] + line[-i-1])

            if threeletter in strings:
                word = threeletter
            elif fourletter in strings:
                word = fourletter
            elif fiveletter in strings:
                word = fiveletter

    except:
        pass

    return word


def main():
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

print(main())