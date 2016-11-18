def to_roman(number):
    sortword1 = sorted(word1)   
    sortword2 = sorted(word2)
    if sortword1 == sortword2:
        return "TRUE"
    else:
        return "FALSE"
def main():
    y = to_roman(15)
    print(y)
if __name__ == '__main__':
    main()



