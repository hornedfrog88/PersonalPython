# I am not sure that I fully understood the directions for this coding assignment
def create_dictionary(lower,upper):
    diction1 = {}
    if upper <= lower:
        print('the lower value has to be less than the upper value')
        return
    else:
        if lower%2 == 0:
            bottomindex = "even"
        else:
            bottomindex = "odd"
        if upper%2 == 0:
            topindex = "even"
        else:
            topindex = "odd"
        diction1 = {bottomindex:lower,topindex:upper}
        return diction1
def main():
	y = create_dictionary(7,14)
	print(y)
if __name__ == '__main__':
	main()




