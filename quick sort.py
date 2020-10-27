from timeit import default_timer as timer

def quicksort(mainlist):
    sorthelp(mainlist,0,len(mainlist)-1)

def sorthelp(mainlist,first,last):
   if first<last:

       midpoint = partition(mainlist,first,last)

       sorthelp(mainlist,first,midpoint-1)
       sorthelp(mainlist,midpoint+1,last)


def partition(mainlist,first,last):
   pivotvalue = mainlist[last]

   i = first-1
   for j in range(first,last):
       if mainlist[j] <= pivotvalue:
           i = i + 1
           swap = mainlist[i]
           mainlist[i] = mainlist[j]
           mainlist[j] = swap


   swap = mainlist[i+1]
   mainlist[i+1] = mainlist[last]
   mainlist[last] = swap
   return i+1
   
liste2=[2,3,-5,1,3,8,-66,-46,9,57,12,45,76,54,4,45,49,45,54,3,764,76,54,457,9,0,98,7,66]
liste=[23,34,-52,13,37,89,-660,-486,98,578,127,453,726,54,41,452,429,435,544,35,5764,76,54,457,9,20,98,7,66]


liste = [0]*1000

def descending(liste):
    for i in range(0,len(liste)):
        liste[i] = len(liste) - i
        
descending(liste)
start = timer()
quicksort(liste)

end = timer()

print(end-start)
