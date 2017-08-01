"""
Assignment: Type List
Write a program that takes a list and prints a message for each element in the
list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type.
If the item is a string, concatenate it onto a new string.
If it is a number, add it to a running sum.
At the end of your program print the string, the number and an analysis of what the list contains.
If it contains only one type, print that type, otherwise, print 'mixed'.
"""

def TypeList(aList) :
    sum = 0;
    outList = []
    foundInt = False
    foundStr = False
    if isinstance(aList, list) :
        for anObj in aList:
            if ( isinstance( anObj, int )):
                sum += anObj
                foundInt = True;
                # print ("This is a int: " + str(anObj))
            elif ( isinstance( anObj, float )):
                sum += anObj
                foundInt = True;
                # print ("This is a float: " + str(anObj))
            elif ( isinstance( anObj, basestring )):
                outList.append (anObj + " ")
                foundStr = True;
                # print ("This is a string: " + str(anObj))
            else :
                print ("    I don't know what object this is: " + str(anObj) )
    else:
        print("You must send me an item of type list.")

    if (foundInt) & (foundStr):
        print ("The list you entered is of mixed type")
    elif (foundInt) & (not foundStr):
        print ("The list you entered is of integer type")
    elif (not foundInt) & (foundStr):
        print ("The list you entered is of string type")
    else:
        print ("The list you entered is neither string or integer type.  :( ")

    if (foundStr):
        s = ""
        print("  String: {0}".format(s.join(outList)));

    if (foundInt):
        print("  Sum: {0}".format(sum))

TypeList(["aString", 93])
print(" ")
print(" ")
"""
Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?
#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"
"""
l = ['magical unicorns',19,'hello',98.98,'world']
TypeList(l)
print(" ")
print(" ")

"""
# input
l = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"
"""
l = [2,3,1,7,4,12]
TypeList(l)
print(" ")
print(" ")

"""
# input
l = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns"
"""

l = ['magical','unicorns']
TypeList(l)
