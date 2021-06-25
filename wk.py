import wikipedia
import sys

def paramet(x, y, z):
	sentenc = x
	wikipedia.set_lang(y)
	search = z
	pages = wikipedia.page(search)
	print(pages.title, "\n")
	print(wikipedia.summary(search, sentences=sentenc))
	print("\n%s\n"%pages.url)

if(len(sys.argv)==1):
		print("\nwk [search]")
		print("wk -n 5 [search]\n\tnumber of lines.")
		print("wk -l pt [search]\n\tlanguage portuguese or out language")
		print("wk -n 10 -l jp search or wk -l es -n 1 [search]\n")
elif(len(sys.argv)>1):
	if(sys.argv[1] == "-n"):
		if(sys.argv[3] == "-l"):
			paramet(sys.argv[2], sys.argv[4], sys.argv[5])
		else:
			paramet(sys.argv[2], "en", sys.argv[3])
	elif(sys.argv[1] == "-l"):
		if(sys.argv[3] == "-n"):
			paramet(sys.argv[4], sys.argv[2], sys.argv[5])
		else:
			paramet(20, sys.argv[2], sys.argv[3])
	else:
		paramet(20, "en", sys.argv[1])
	