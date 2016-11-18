def combine_and_sort(list1,list2):
    clist = list1+list2
    clist.sort()
    return clist
def main():
	y = combine_and_sort([1,6,3,14,6],[9,44,83,12])
	print(y)
if __name__ == '__main__':
	main()




