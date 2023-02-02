def myFun(*argv):
	for arg in argv:
		print(arg)


myFun("vishal", "vishu", "sharma")


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='vishu', mid='vini', last='vishal')