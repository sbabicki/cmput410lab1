class MyClass:
    variable = "blah"
    def addition(self, x,y):
        """
        testing:
        >>> c = MyClass()
        blah
        >>> print c.addition(3,4)
        7
        """
        return x+y
    def __init__(self):
        print self.variable

c = MyClass()
print c.addition(3,4)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
phoneBook = {}
phoneBook["A"] = 111111
phoneBook["B"] = 222222
phoneBook["C"] = 333333

for name, number in phoneBook.items():
    print "Phone number of %s is %d" %(name, number)
del phoneBook["A"]

print "======"
for name, number in phoneBook.items():
    print "Phone number of %s is %d" %(name, number)
    

def do_stuff_with_number(n, list1):
    print list1[n]
    
list1 = [1,2,3,7,2,4]
for i in range(10):
    try:
        do_stuff_with_number(i, list1)
    except IndexError:
        print 0
        # print "Index Error"
        # do_stuff_with_number(0, list1)