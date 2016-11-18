def check_anagram(word1,word2):
    sortword1 = sorted(word1)   
    sortword2 = sorted(word2)
    if sortword1 == sortword2:
        return "TRUE"
    else:
        return "FALSE"
def main():
    y = check_anagram('crabby','rcabyb')
    print(y)
if __name__ == '__main__':
    main()



