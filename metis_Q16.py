def arr(lower,upper):
    if upper <= lower:
        print('the lower value has to be less than the upper value')
        return
    else:
        if lower%2 == 0:
            bottom = lower
        else:
            bottom = lower+1
        if upper%2 == 0:
            top = upper
        else:
            top = upper-1
        c = [bottom]
        counter = 2
        while (counter+bottom) <= top:
            c.append(bottom+counter)
            counter = counter+2
        return c
def main():
	y = arr(7,17)
	print(y)
if __name__ == '__main__':
	main()




