import random
def main():
    match = False
    maincounter = 1
    color = ['red','orange','blue','pink','black','white','burgundy','magenta','purple','yellow','green','lavender','turquoise','gray','maroon']
    words = ['inky','binky','bonky','daddy','had','a','donkey']
    while not match:
        innerlooper = 0
        statement = []
        while innerlooper < 7:
            randomnumber = random.randint(0,6)
            statement.append(words[randomnumber])
            innerlooper += 1
        fullstatement = ' '.join(statement)
        print(fullstatement)
        print(maincounter)
        maincounter += 1
        if fullstatement == 'inky binky bonky daddy had a donkey':
            print(maincounter)
            match = True
main()

########################################### Testing the average of how many times it takes to randomly match binky binky binky
import random
def main():
    counterlist = []
    color = ['red','orange','blue','pink','black','white','burgundy','magenta','purple','yellow','green','lavender','turquoise','gray','maroon']
    words = ['inky','binky','bonky']
    for x in range(1,100000):
        match = False
        maincounter = 1
#        print('top loop=',x)
        while not match:
#            print(maincounter)
            innerlooper = 0
            statement = []
            while innerlooper < 3:
                randomnumber = random.randint(0,2)
                statement.append(words[randomnumber])
                innerlooper += 1
            fullstatement = ' '.join(statement)
#            print(fullstatement)
            maincounter += 1
            if fullstatement == 'binky binky binky':
                match = True
                counterlist.append(maincounter)
    average = sum(counterlist)/x
    print('counterlist = ',average)
main()