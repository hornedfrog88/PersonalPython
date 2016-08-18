def main():
#opens and writes file to c:\users\richard
	f = open("testwritefile.txt","w")
	f.write("Pythonprogramminglanugage.com, \n")
	f.write("Example program., \n")
	f.write("Let's see how data can be written out to a file.")
	f.close()	
main()