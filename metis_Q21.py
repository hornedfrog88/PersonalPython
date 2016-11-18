def to_roman(numeral):
    charnumeral = str(numeral)
    strlength = len(charnumeral)
    onespostuple = ('I','II','III','IV','V','VI','VII','VIII','IX')
    tenspostuple = ('X','XX','XXX','XL','L','LX','LXX','LXXX','XC')
    hundspostuple = ('C','CC','CCC','CD','D','DC','DCC','DCCC','CM') 
    onesroman = ''
    tensroman = ''
    hundsroman = ''
    if numeral > 1000:
        return "Number entered is out of range"
    elif numeral == 1000:
        return 'M'
#Ones
    if strlength == 1:
        for i in range(0,9):
            if i + 1 == numeral:
                return onespostuple[i]
#Tens
    if strlength == 2:
        numeral1 = int(charnumeral[0])
        numeral2 = int(charnumeral[1])
        for i in range(0,9):
            if i + 1 == numeral1:
                tensroman = tenspostuple[i]
        if numeral2 > 0:
            for k in range(0,9):
                if k + 1 == numeral2:
                    onesroman = onespostuple[k]
        else:
            onesroman = ''
        return tensroman+onesroman
#Hundreds
    if strlength == 3:
        numeral1 = int(charnumeral[0])
        numeral2 = int(charnumeral[1])
        numeral3 = int(charnumeral[2])      
        for i in range(0,9):
            if i + 1 == numeral1:
                hundsroman = hundspostuple[i]
        if numeral2 > 0:
            for j in range(0,9):
                if j + 1 == numeral2:
                    tensroman = tenspostuple[j]
        else:
            tensroman = '' 
        if numeral3 > 0:
            for k in range(0,9):
                if k + 1 == numeral3:
                    onesroman = onespostuple[k]
        else:
            onesroman = ''
        return hundsroman+tensroman+onesroman

def main():
    y = to_roman(1000)
    print(y)
if __name__ == '__main__':
    main()


