def from_roman(roman):
    strlength = len(roman)
    romandictionary = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if strlength == 1:
            return romandictionary[roman]
    if strlength > 1:
        runningtotal = 0
        counter = strlength
        for i in range(0,counter):
            runningtotal = runningtotal + romandictionary[roman[i]]
    four = 'IV'
    nine = 'IX'
    forty = 'XL'
    ninety = 'CX'
    fourhundred = 'CD'
    ninehundred = 'CM'
    decrement1 = 0
    decrement2 = 0
    decrement3 = 0
    if four in roman:
        decrement1 = 2
    if nine in roman:
        decrement1 = 2
    if forty in roman:
        decrement2 = 20
    if ninety in roman:
        decrement2 = 20
    if fourhundred in roman:
        decrement3 = 200
    if ninehundred in roman:
        decrement3 = 200
    totaldecrement = decrement1+decrement2+decrement3
    runningtotal = runningtotal-totaldecrement
    return runningtotal
def main():
    y = from_roman('CMXLIV')
    print(y)
if __name__ == '__main__':
    main()


