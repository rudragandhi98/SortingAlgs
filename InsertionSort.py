from timeit import default_timer as timer

# Insertion Sort
file2 = open('20k.txt', 'r')
sortedLines = file2.readlines()
sortedLines.sort() # Using a library Function, to sort the array, this will be used to check my implementation

start = timer()
file1 = open('20k.txt', 'r')
Lines = file1.readlines()

#Implementing Insertion Sort
for i in range(1,len(Lines)):
    key = Lines[i]
    j = i-1
    while( j >= 0 and key < Lines[j]) :
        Lines[j+1] = Lines[j]
        j = j - 1
    Lines[j+1] = key


end = timer()
print(Lines)
print(Lines == sortedLines) # Comparing to check if my implementation gives a sorted array.
print(end-start) # Finding the total time measurement