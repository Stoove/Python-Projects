## Script in which I explore some of the useful/problematic features of lists.
## The top section is my own experimentation. The bottom section is partially copied (and partially improvised)
## from the MIT OpenCourseware series.

myList = [1,2,3]

x = myList[0]

print('x = ' + str(x))

myList[0] = 12

## Show that changing a list element does not affect the value of the immutable x
print('x = ' + str(x))

List2 = [myList,myList]
print('List2 = ' + str(List2))

## Show that changing myList will change the values in List2
myList[0] = 23
print('myList = ' + str(myList))
print('List2 = ' + str(List2))

## Show that this is the same in reverse by modifying an element of List2
List2[0][0] = 'nine'
print('myList = ' + str(myList))
print('List2 = ' + str(List2))

## Show that this is not true when I replace List2[0] with a new object/value entirely
List2[0] = ['changed',2,3]
print('myList = ' + str(myList))
print('List2 = ' + str(List2))



####################################################



## Here is some sample code from the MIT OpenCourseware Intro.Comp.Sci. (2011) course, which I am following along with

techs = ['MIT','Cal Tech']
Ivys = ['Harvard','Yale','Brown']

## Showing nesting lists
Univs = [techs,Ivys]
print('Techs = ' + str(techs))
print('Ivys = ' + str(Ivys))
print('Univs = ' + str(Univs))

## Showing list concatentation
flat = techs + Ivys
print('Techs = ' + str(techs))
print('Ivys = ' + str(Ivys))
print('flat = ' + str(flat))


## Using a for loop and if statement to remove degenerate names in the list flat before concatenation
artSchools = ['RISD','Harvard']
for u2 in artSchools:
    if u2 in flat:
        flat.remove(u2)

flat = flat + artSchools

print('artSchools = ' + str(artSchools))
print('flat = ' + str(flat))

## Sorting flat
flat.sort() ## NB: Calling flat = flat.sort() does not return a sorted flat!
print('flat = ' + str(flat))

## Showing again that manipulation of one list affects another list it's bound to
L1 = [2]
L2 = [L1,L1]
print('L1 = ' + str(L1))
print('L2 = ' + str(L2))

L1[0] = 3
print('L1 = ' + str(L1))
print('L2 = ' + str(L2))

## Define a function CopyList, which copies the elements of lSource to lDest without linking the lists

def CopyList(lSource,lDest):
    for e in lSource:
        lDest.append(e)
        print('lDest = ' + str(lDest))

L1 = []
L2 = [1,2,3]

CopyList(L2,L1)
print('L1 = ' + str(L1))
print('L2 = ' + str(L2))
















